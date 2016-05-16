#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of clustering with K-Means
"""

import em
import numpy as np
import scipy.spatial
import scipy.linalg
cdist = scipy.spatial.distance_matrix

class KMeansClusterer(em.EMAlgorithm):
    """
    Clusterer using the K-means algorithm
    """

    def __init__(self, K, D):
        self.K, self.D = K, D
        em.EMAlgorithm.__init__(self)

    def compute_expectation(self, X, O):
        """Compute the most likely values of the latent variables;
        @X - data (N*D)
        @O - current cluster centers (K*D)
        @returns lhood, cluster assignments"""
        N, D = X.shape
        K, D_ = O.shape
        assert D == self.D
        assert D_ == self.D
        assert K == self.K

        total_lhood = 0
        # Get pairwise distances between centers (D_ij = \|X_i - M_j\|)
        D = cdist(X, O)
        # Assignments
        Z = D.argmin(axis=1)
        total_lhood += ((X - O[Z])**2).sum() / N # Average distance as measure.

        return -total_lhood, Z

    def compute_maximisation(self, X, Z, O):
        """Compute the most likely values of the parameters"""
        N, D = X.shape
        N_, = Z.shape
        assert N == N_
        assert D == self.D

        O = np.vstack([X[Z==k].mean(0) for k in range(self.K)])

        return O

    @staticmethod
    def kmeanspp_initialisation(X, K):
        """Initialise means using K-Means++
        @X:np.array a N * D matrix.
        @returns:np.array -  a K * D matrix.
        """
        N, D = X.shape

        M = []
        # Choose one center amongst the X at random
        m = np.random.randint(N)
        M.append(X[m])

        # Choose k centers
        while len(M) < K:
            # Create a probability distribution D^2 from the previous mean
            D = cdist(X, M).min(1)**2
            assert D.shape == (N,)

            # Normalise and sample a new point
            D /= D.sum()

            m = np.random.multinomial(1, D).argmax()
            M.append(X[m])

        return np.vstack( M )

    def run( self, X, O = None, *args, **kwargs ):
        """O are the 'true' parameters"""
        if O == None:
            O = KMeansClusterer.kmeanspp_initialisation( X, self.K )
        return em.EMAlgorithm.run( self, X, O, *args, **kwargs )

def test_kmeans():
    """
    Test whether kmeans works or not.
    """
    K = 3
    D = 2
    mvn = np.random.multivariate_normal

    # Generate data
    O = np.array([[-1,-1],[0,0],[1,1]])
    X = np.vstack([mvn(o, 0.5*np.eye(D), size=10000) for o in O]) 

    algo = KMeansClusterer(K, D)
    lhood, Z, O_ = algo.run(X)
    print(O)
    print(lhood)
    print(Z)
    print(O_)

