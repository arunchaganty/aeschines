#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
An EM algorithm for GMMs
"""

import numpy as np
import scipy as sc
import scipy.misc
import scipy.spatial
import scipy.linalg

from numpy import array, eye, ones, log
from scipy.linalg import norm
cdist = scipy.spatial.distance.cdist
logsumexp = scipy.logaddexp.reduce

from . import em

from .KMeansClustering import KMeansClusterer

class GaussianMixtureClusterer(em.EMAlgorithm):
    """
    Gaussian Mixtures EM
    (i) Using k-means++ start
    (ii) Assuming spherical gaussians
    """

    def __init__( self, k, d ):
        self.K, self.D = k, d
        em.EMAlgorithm.__init__( self )

    def compute_expectation( self, X, O ):
        """Compute the most likely values of the latent variables; returns lhood"""
        _, d = X.shape
        M, sigma, w = O

        total_lhood = 0
        # Get pairwise distances between centers (D_ij = \|X_i - M_j\|)
        D = cdist( X, M )
        # Probability dist = 1/2(\sigma^2) D^2 + log w
        Z = - 0.5/sigma**2 * (D**2) + log( w ) - 0.5 * d * log(sigma) # Ignoreing constant term
        total_lhood += logsumexp( logsumexp(Z) )

        # Normalise the probilities (soft EM)
        Z = sc.exp(Z.T - logsumexp(Z, 1)).T
            
        return -total_lhood, Z

    def compute_maximisation( self, X, Z, O ):
        """Compute the most likely values of the parameters"""
        N, d = X.shape

        M, sigma, w = O

        # Cluster weights (smoothed)
        # Pseudo counts
        w = Z.sum(axis=0) + 1

        # Get new means
        M = (Z.T.dot( X ).T / w).T
        sigma = (cdist( X, M ) * Z).sum()/(d*N)
        w /= w.sum()

        return M, sigma, w

    @staticmethod
    def kmeanspp_initialisation(X, K):
        """Initialise means using K-Means++"""
        N, D = X.shape
        M = KMeansClusterer.kmeanspp_initialisation(X, K)
        sigma = cdist( X, M ).sum()/(K*D*N)
        w = ones(K)/float(K)

        return M, sigma, w



    def run( self, X, O = None, *args, **kwargs ):
        """O are the 'true' parameters"""
        if O == None:
            O = GaussianMixtureClusterer.kmeanspp_initialisation( X, self.K )
        return em.EMAlgorithm.run( self, X, O, *args, **kwargs )

def test_gmm():
    """
    Test whether gmm works or not.
    """
    K = 3
    D = 2
    mvn = np.random.multivariate_normal

    # Generate data
    O = np.array([[-1,-1],[0,0],[1,1]])
    X = np.vstack([mvn(o, 0.5*np.eye(D), size=10000) for o in O]) 

    algo = GaussianMixtureClusterer(K, D)
    lhood, Z, O_ = algo.run(X)
    print(O)
    print(lhood)
    print(O_[0])

