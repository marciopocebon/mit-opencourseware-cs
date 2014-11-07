# 6.00 Problem Set 5
# RSS Feed Filter

import feedparser
import string
import re
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory:
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_subject(self):
        return self.subject

    def get_summary(self):
        return self.summary

    def get_link(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

class WordUtils():

    @staticmethod
    def remove_punctuation(text):
        # print 'iniail ', text
        for punctuation in string.punctuation:
            text = text.replace(punctuation, ' ')

        # print 'final ', text

        return text

    @staticmethod
    def normalize_text(text):
        return WordUtils.remove_punctuation(text).split(' ')

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word;

    def is_word_in(self, text):
        text = WordUtils.normalize_text(text)

        for text_word in text:
            if self.word.lower() == text_word.lower():
                return True

        return False

class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        title = story.get_title()

        return self.is_word_in(title)

class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        subject = story.get_subject()

        return self.is_word_in(subject)
# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        summary = story.get_summary()

        return self.is_word_in(summary)

# Composite Triggers
# Problems 6-8

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, news_item):
        return not self.trigger.evaluate(news_item)

class AndTrigger(Trigger):
    def __init__(self, trigger_a, trigger_b):
        self.trigger_a = trigger_a
        self.trigger_b = trigger_b

    def evaluate(self, news_item):
        return self.trigger_a.evaluate(news_item) and self.trigger_b.evaluate(news_item)

class OrTrigger(Trigger):
    def __init__(self, trigger_a, trigger_b):
        self.trigger_a = trigger_a
        self.trigger_b = trigger_b

    def evaluate(self, news_item):
        return self.trigger_a.evaluate(news_item) or self.trigger_b.evaluate(news_item)

# Phrase Trigger
# Question 9

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def is_phrase_in(self, text):
        return self.phrase in text

    def evaluate(self, story):
        title_trigger = TitleTrigger(self.phrase)
        subject_trigger = SubjectTrigger(self.phrase)
        summary_trigger = SummaryTrigger(self.phrase)

        return self.is_phrase_in(story.get_title()) or self.is_phrase_in(story.get_summary()) or self.is_phrase_in(story.get_subject())

#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """

    filtered_stories = []

    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filtered_stories.append(story)
                break

    return filtered_stories

#======================
# Part 4
# User-Specified Triggers
#======================
TRIGGERS = {
    'TITLE': TitleTrigger,
    'SUBJECT': SubjectTrigger,
    'PHRASE': PhraseTrigger,
    'AND': AndTrigger,
    'OR': OrTrigger,
    'NOT': NotTrigger
}

def getValidLinesFromFile(filename):
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)
    return lines

def get_trigger(line):
    for name in TRIGGERS:
        if name in line:
            return TRIGGERS[name]

def build_triggers(lines):
    triggers = []
    for line in lines:
        trigger = get_trigger(line)
        triggers.append(trigger)

    return triggers

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    lines = getValidLinesFromFile(filename)
    lines = build_triggers(lines)

    print lines

print readTriggerConfig('triggers.txt')

# import thread

# def main_thread(p):
#     # A sample trigger list - you'll replace
#     # this with something more configurable in Problem 11
#     t1 = SubjectTrigger("Obama")
#     t2 = SummaryTrigger("MIT")
#     t3 = PhraseTrigger("Supreme Court")
#     t4 = OrTrigger(t2, t3)
#     triggerlist = [t1, t4]

#     # TODO: Problem 11
#     # After implementing readTriggerConfig, uncomment this line
#     #triggerlist = readTriggerConfig("triggers.txt")

#     guidShown = []

#     while True:
#         print "Polling..."

#         # Get stories from Google's Top Stories RSS news feed
#         stories = process("http://news.google.com/?output=rss")
#         # Get stories from Yahoo's Top Stories RSS news feed
#         stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

#         # Only select stories we're interested in
#         stories = filter_stories(stories, triggerlist)

#         # Don't print a story if we have already printed it before
#         newstories = []
#         for story in stories:
#             if story.get_guid() not in guidShown:
#                 newstories.append(story)

#         for story in newstories:
#             guidShown.append(story.get_guid())
#             p.newWindow(story)

#         print "Sleeping..."
#         time.sleep(SLEEPTIME)

# SLEEPTIME = 60 #seconds -- how often we poll
# if __name__ == '__main__':
#     p = Popup()
#     thread.start_new_thread(main_thread, (p,))
#     p.start()

