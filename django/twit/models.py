from django.db import models
import datetime
from html import unescape
import ipdb
import math

DT_FORMAT = "%a %b %d %H:%M:%S %z %Y"

def clean_string(inp):
    if inp is None: return ""
    return unescape(inp).strip().replace('\n',' ').replace('\r', '')

class User(models.Model):
    """Twitter's user object"""
    id = models.BigIntegerField(primary_key=True, help_text='Unique id that comes from Twitter')
    name = models.CharField(max_length=512, help_text='Full user name')
    created_at = models.DateTimeField(help_text='Time tweet was created')
    location = models.TextField(null=True, help_text='String description of location')
    followers_count = models.IntegerField(default=0, help_text='Number of followers')
    verified = models.BooleanField(help_text='Is the user verified')
    time_zone = models.TextField(null=True, help_text='Timezone used by user')
    description = models.TextField(null=True, help_text='Description of user')
    statuses_count = models.IntegerField(help_text='Number of status updates by user')
    friends_count = models.IntegerField(help_text='Number of friends')
    screen_name = models.CharField(max_length=512, help_text='Short user name')

    @staticmethod
    def from_json(obj):
        return User(
            id = obj['id'],
            name = obj['name'],
            created_at = datetime.datetime.strptime(obj['created_at'], DT_FORMAT),
            location = obj['location'],
            followers_count = int(obj['followers_count']),
            verified = bool(obj['verified']),
            time_zone = obj['time_zone'],
            description = obj['description'],
            statuses_count = int(obj['statuses_count']),
            friends_count = int(obj['friends_count']),
            screen_name = obj['screen_name'],)

    @staticmethod
    def from_json_to_tsv_header():
        return [
            'id',
            'name',
            'created_at',
            'location',
            'followers_count',
            'verified',
            'time_zone',
            'description',
            'statuses_count',
            'friends_count',
            'screen_name',]

    @staticmethod
    def from_json_to_tsv(obj):
        return [
            obj['id'],
            obj['name'],
            obj['created_at'],
            obj['location'],
            int(obj['followers_count']),
            bool(obj['verified']),
            obj['time_zone'],
            clean_string(obj['description']),
            int(obj['statuses_count']),
            int(obj['friends_count']),
            obj['screen_name'],]

    def update_or_create(self):
        return User.objects.update_or_create(
            id=self.id,
            defaults = {
                'name' : self.name,
                'created_at' : self.created_at,
                'location' : self.location,
                'followers_count' : self.followers_count,
                'verified' : self.verified,
                'time_zone' : self.time_zone,
                'description' : self.description,
                'statuses_count' : self.statuses_count,
                'friends_count' : self.friends_count,
                'screen_name' : self.screen_name,})

    def __str__(self):
        return self.screen_name

    def __repr__(self):
        return "[User: " + self.screen_name + "]"

class Tweet(models.Model):
    """Tweet object"""
    id = models.BigIntegerField(primary_key=True, help_text='Unique id that comes from Twitter')
    created_at = models.DateTimeField(help_text='Time tweet was created')
    text = models.CharField(max_length=256, help_text='Raw text context of tweet')
    retweet_count = models.IntegerField(help_text='Count of retweets')
    favorite_count = models.IntegerField(default=0,help_text='Count of favorites')
    reply_to_id = models.BigIntegerField(default=-1, help_text='Reference to an existing tweet (may not be in database)', null=True)
    user = models.ForeignKey(User)

    @property
    def reply_to(self):
        """Try to get reply to tweet"""
        try:
            return Tweet.objects.get(id = self.reply_to_id)
        except Tweet.ObjectDoesNotExist:
            return None

    @property
    def url(self):
        return "https://twitter.com/{}/status/{}".format(self.user.screen_name, self.id)

    @staticmethod
    def from_json(obj):
        user, _ = User.from_json(obj['user']).update_or_create()
        return Tweet(
            id = obj['id'],
            created_at = datetime.datetime.strptime(obj['created_at'], DT_FORMAT), # "Mon Sep 24 03:35:21 +0000 2012"
            text = clean_string(obj['text']),
            retweet_count = obj['retweet_count'],
            favorite_count = obj['favorite_count'],
            reply_to_id = obj['in_reply_to_status_id'],
            user = user)

    @staticmethod
    def from_json_to_tsv_header():
        return [
            'id',
            'created_at', # "Mon Sep 24 03:35:21 +0000 2012"
            'text',
            'retweet_count',
            'favorite_count',
            'reply_to_id',
            'user_id',]

    @staticmethod
    def from_json_to_tsv(obj):
        return [
            obj['id'],
            obj['created_at'], # "Mon Sep 24 03:35:21 +0000 2012"
            clean_string(obj['text']),
            obj['retweet_count'],
            obj['favorite_count'],
            obj['in_reply_to_status_id'],
            obj['user']['id']]

    def to_tsv(self):
        return [
            self.id,
            self.created_at,
            self.text,
            self.retweet_count,
            self.favorite_count,
            self.reply_to_id,
            self.user]

    def update_or_create(self):
        return Tweet.objects.update_or_create(
            id=self.id,
            defaults = {
                'created_at' : self.created_at,
                'text' : self.text,
                'retweet_count' : self.retweet_count,
                'favorite_count' : self.favorite_count,
                'reply_to_id' : self.reply_to_id,
                'user' : self.user,
                })

    @staticmethod
    def is_retweet(jsonobj):
        """Is this blob a retweet?"""
        return "retweeted_status" in jsonobj

    def __str__(self):
        return self.text

    def __repr__(self):
        return "[Tweet: " + self.text[:40] + "...]"

class Retweet(models.Model):
    """retweet object"""
    id = models.BigIntegerField(primary_key=True, help_text='Unique id that comes from Twitter')
    tweet = models.ForeignKey(Tweet)
    created_at = models.DateTimeField(help_text='Time tweet was created')
    user = models.ForeignKey(User)

    @property
    def url(self):
        return "https://twitter.com/{}/status/{}".format(self.user.screen_name, self.id)

    @staticmethod
    def from_json(obj):
        """
        Assembles a retweet.
        Original tweet has an updated retweet and favorite count, and this should be saved.
        @Returns retweet, original tweet
        """
        assert Tweet.is_retweet(obj)

        tweet, _ = Tweet.from_json(obj['retweeted_status']).update_or_create()
        user, _ = User.from_json(obj['user']).update_or_create()
        retweet = Retweet(
            id = obj['id'],
            tweet = tweet,
            created_at = datetime.datetime.strptime(obj['created_at'], DT_FORMAT),
            user = user)
        return retweet

    def update_or_create(self):
        return Retweet.objects.update_or_create(
            id=self.id,
            defaults = {
                'tweet' : self.tweet,
                'created_at' : self.created_at,
                'user' : self.user,
                })

    @staticmethod
    def from_json_to_tsv_header():
        """Translate json to TSV"""
        return [
            'id',
            'tweet_id',
            'created_at',
            'user_id']

    @staticmethod
    def from_json_to_tsv(obj):
        """Translate json to TSV"""
        return [
            obj['id'],
            obj['retweeted_status']['id'],
            obj['created_at'],
            obj['user']['id']]
    def __str__(self):
        return "RT:" + self.tweet.text

    def __repr__(self):
        return "[Retweet: " + self.tweet.text[:40] + "...]"

class Mention(models.Model):
    """
    Entity mentioned in model
    """
    tweet = models.ForeignKey(Tweet, help_text='Tweet containing this entity')
    type = models.CharField(max_length=16, help_text='Type of entity')
    text = models.CharField(max_length=256)
    doc_char_begin = models.IntegerField(help_text='Character offset in tweet')
    doc_char_end = models.IntegerField(help_text='Character offset in tweet')

    @staticmethod
    def from_json(obj, type, tweet):
        return Mention(
            tweet = tweet,
            type = type,
            text = obj['text'],
            doc_char_begin = obj['indices'][0],
            doc_char_end = obj['indices'][1],)

class UserMention(Mention):
    """
    User mentioned in model
    """
    user_id = models.BigIntegerField(User, help_text='User mentioned in the tweet')

    @property
    def user(self):
        """Try to get model"""
        try:
            return User.objects.get(id = self.user_id)
        except User.ObjectDoesNotExist:
            return None

    @staticmethod
    def from_json(obj, tweet):
        return UserMention(
            tweet = tweet,
            type = 'user_mention',
            text = obj['screen_name'],
            doc_char_begin = obj['indices'][0],
            doc_char_end = obj['indices'][1],
            user_id = obj['id']
            )

class EntityMention(models.Model):
    """
    Identifies a mention of an entity within a tweet.
    """
    tweet = models.ForeignKey(Tweet)
    doc_char_begin = models.IntegerField()
    doc_char_end = models.IntegerField()
    gloss = models.TextField()
    best_entity = models.TextField()

    def __str__(self):
        return self.best_entity

    def __repr__(self):
        return "[Entity: {}]".format(self.best_entity)

class EntityStance(models.Model):
    """
    Identifies the purported stance of the specified entity.
    """
    tweet = models.ForeignKey(Tweet, related_name="stances")
    entity = models.TextField(help_text='Entity with stance')
    stance = models.FloatField(help_text='Stance value')
    score = models.FloatField(help_text='Confidence of stance value')

    def __str__(self):
        return "{} {:.2f}".format(self.entity, self.stance)

    def __repr__(self):
        return "[Stance: {}={:.2f}]".format(self.entity, self.stance)

class UserStance(models.Model):
    """
    Identifies the purported stance of the specified entity.
    """
    user = models.ForeignKey(User, related_name="stance", primary_key=True)
    hc = models.FloatField(help_text='Hillary Clinton')
    bs = models.FloatField(help_text='Bernie Sanders')
    dt = models.FloatField(help_text='Donald Trump')
    tc = models.FloatField(help_text='Ted Cruz')
    count = models.BigIntegerField(help_text='Number of tweets')
    alignment_score = models.FloatField(help_text='Alignment Score')

    def __str__(self):
        return "{} {:.2f}".format(self.entity, self.stance)

    def __repr__(self):
        return "[Stance: {}={:.2f}]".format(self.entity, self.stance)

    def compute_alignment(self):
        """
        Computes alignment as a crazy entropy based score.
        """
        def normalize(x):
            return 0 if x is None else x
        # First normalize scores to be all positive.
        hc_, bs_, dt_, tc_ = 0, 0, 0, 0
        hc, bs, dt, tc = [normalize(x) for x in [self.hc, self.bs, self.dt, self.tc]]
        if hc < 0:
            dt_ += 0.5
            tc_ += 0.5
        else:
            hc_ += hc
        if bs < 0:
            dt_ += 0.5
            tc_ += 0.5
        else:
            bs_ += bs
        if dt < 0:
            hc_ += 0.5
            bs_ += 0.5
        else:
            dt_ += dt
        if tc < 0:
            hc_ += 0.5
            bs_ += 0.5
        else:
            tc_ += tc
        assert hc_ >= 0 and bs_ >= 0 and dt_ >= 0 and tc_ >= 0

        vals = [hc_, bs_, dt_, tc_]
        vals = [x / max(1e-5,sum(vals)) for x in vals]
        return sum(math.exp(x) * x for x in vals) / math.exp(1)

    class Meta:
        managed = False

class TopicMention(models.Model):
    """
    Identifies which topic the tweet falls into.
    """
    tweet = models.ForeignKey(Tweet, related_name="topics")
    topic = models.TextField(help_text='Description of a topic.')
    score = models.FloatField(help_text='Confidence of class')

    def __str__(self):
        return "{}".format(self.topic)

    def __repr__(self):
        return "[Topic: {}]".format(self.topic)

class StanceTopicSummary(models.Model):
    """
    A view that captures stance and topic
    """
    entity = models.TextField(help_text="")
    stance = models.FloatField(help_text="For/Neutral/Against")
    topic = models.TextField(help_text="")
    count = models.BigIntegerField()

    class Meta:
        managed = False

