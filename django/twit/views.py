
from django.shortcuts import render
#from django.models import Prefetch
from .models import *
from collections import defaultdict, Counter

# Create your views here.
def view_tweets(request, entity=None, stance=None, topic=None):
    print (entity, stance, topic)
    tweets = Tweet.objects.all()
    if entity is not None:
        tweets = tweets.filter(stances__entity = entity)
    if stance is not None:
        tweets = tweets.filter(stances__stance = int(stance))
    if topic is not None:
        tweets = tweets.filter(topics__topic__iregex = topic)
    tweets = tweets[:10].select_related('user__id', 'user__screen_name').prefetch_related('stances', 'topics')

    return render(request, 'list.html', {'tweets' : tweets})

# Create your views here.
def summary(request):
    blob = StanceTopicSummary.objects.all()

    stances = ["↔","↑","↓"]
    candidates = set([])
    topics = set([])
    store = defaultdict(Counter)
    for entry in blob:
        assert entry.stance in [0,-1,1]

        candidates.add(entry.entity)
        topics.add(entry.topic)

        key = entry.entity, stances[int(entry.stance)]
        topic = entry.topic
        count = entry.count

        store[topic][key] = count

    candidates = [(c,s) for c in sorted(candidates) for s in stances]
    topics = list(sorted(topics))
    counts = [(topic, [store[topic][key] for key in candidates]) for topic in topics]
    candidates = ["".join(key) for key in candidates]

    return render(request, 'summary.html', {
        'candidates' : candidates,
        'topics' : topics,
        'counts' : counts})
