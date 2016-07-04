"""praw constants."""

__version__ = '4.0.0b5'

API_PATH = {
    'accept_mod_invite':   'api/accept_moderator_invite',
    'access_token_url':    'api/v1/access_token/',
    'approve':             'api/approve/',
    'authorize':           'api/v1/authorize/',
    'banned':              'r/{subreddit}/about/banned/',
    'blocked':             'prefs/blocked/',
    'by_id':               'by_id/',
    'captcha':             'captcha/',
    'clearflairtemplates': 'api/clearflairtemplates/',
    'collapse_message':    'api/collapse_message/',
    'comment':             'api/comment/',
    'comment_replies':     'message/comments/',
    'comments':            'comments/',
    'compose':             'api/compose/',
    'contest_mode':        'api/set_contest_mode/',
    'contributor':         'r/{subreddit}/about/contributors/',
    'controversial':       'controversial/',
    'default_subreddits':  'subreddits/default/',
    'del':                 'api/del/',
    'deleteflair':         'api/deleteflair',
    'delete_redditor':     'api/delete_user',
    'delete_sr_header':    'r/{subreddit}/api/delete_sr_header',
    'delete_sr_image':     'r/{subreddit}/api/delete_sr_img',
    'distinguish':         'api/distinguish/',
    'domain':              'domain/{domain}/',
    'duplicates':          'duplicates/{submission_id}/',
    'edit':                'api/editusertext/',
    'edited':              'r/{subreddit}/about/edited/',
    'flair':               'r/{subreddit}/api/flair/',
    'flairconfig':         'api/flairconfig/',
    'flaircsv':            'r/{subreddit}/api/flaircsv/',
    'flairlist':           'r/{subreddit}/api/flairlist/',
    'flairselector':       'api/flairselector/',
    'flairtemplate':       'api/flairtemplate/',
    'friend':              'api/friend/',
    'friend_v1':           'api/v1/me/friends/{user}',
    'friends':             'api/v1/me/friends/',
    'gild_thing':          'api/v1/gold/gild/{fullname}/',
    'gild_user':           'api/v1/gold/give/{username}/',
    'help':                'help/',
    'hide':                'api/hide/',
    'ignore_reports':      'api/ignore_reports/',
    'inbox':               'message/inbox/',
    'info':                'api/info/',
    'leavecontributor':    'api/leavecontributor',
    'leavemoderator':      'api/leavemoderator',
    'me':                  'api/v1/me',
    'mentions':            'message/mentions',
    'message':             'message/messages/{messageid}/',
    'messages':            'message/messages/',
    'moderator':           'r/{subreddit}/about/moderators/',
    'modlog':              'r/{subreddit}/about/log/',
    'modqueue':            'r/{subreddit}/about/modqueue/',
    'mod_mail':            'r/{subreddit}/message/moderator/',
    'morechildren':        'api/morechildren/',
    'my_con_subreddits':   'subreddits/mine/contributor/',
    'my_mod_subreddits':   'subreddits/mine/moderator/',
    'my_multis':           'api/multi/mine/',
    'my_subreddits':       'subreddits/mine/subscriber/',
    'new':                 'new/',
    'new_subreddits':      'subreddits/new/',
    'marknsfw':            'api/marknsfw/',
    'multireddit':         'user/{user}/m/{multi}/',
    'multireddit_add':     'api/multi/user/{user}/m/{multi}/r/{subreddit}',
    'multireddit_about':   'api/multi/user/{user}/m/{multi}/',
    'multireddit_copy':    'api/multi/copy/',
    'multireddit_mine':    'me/m/{multi}/',
    'multireddit_rename':  'api/multi/rename/',
    'multireddit_user':    'api/multi/user/{user}/',
    'mute_sender':         'api/mute_message_author/',
    'muted':               'r/{subreddit}/about/muted/',
    'popular_subreddits':  'subreddits/popular/',
    'read_message':        'api/read_message/',
    'reddit_url':          '/',
    'register':            'api/register/',
    'remove':              'api/remove/',
    'report':              'api/report/',
    'reports':             'r/{subreddit}/about/reports/',
    'rising':              'rising/',
    'save':                'api/save/',
    'saved':               'saved/',
    'search':              'r/{subreddit}/search/',
    'search_reddit_names': 'api/search_reddit_names/',
    'select_flair':        'api/selectflair/',
    'sent':                'message/sent/',
    'sticky':              'r/{subreddit}/about/sticky/',
    'sticky_submission':   'api/set_subreddit_sticky/',
    'site_admin':          'api/site_admin/',
    'spam':                'r/{subreddit}/about/spam/',
    'stylesheet':          'r/{subreddit}/about/stylesheet/',
    'sub_comments_gilded': 'r/{subreddit}/comments/gilded/',
    'sub_recommendations': 'api/recommend/sr/{subreddits}',
    'submission':          'comments/{id}/',
    'submission_replies':  'message/selfreply/',
    'submit':              'api/submit/',
    'subreddit':           'r/{subreddit}/',
    'subreddit_about':     'r/{subreddit}/about/',
    'subreddit_comments':  'r/{subreddit}/comments/',
    'subreddit_css':       'api/subreddit_stylesheet/',
    'subreddit_random':    'r/{subreddit}/random/',
    'subreddit_settings':  'r/{subreddit}/about/edit/',
    'subreddit_traffic':   'r/{subreddit}/about/traffic/',
    'subscribe':           'api/subscribe/',
    'suggested_sort':      'api/set_suggested_sort/',
    'top':                 'top/',
    'uncollapse_message':  'api/uncollapse_message/',
    'unfriend':            'api/unfriend/',
    'unhide':              'api/unhide/',
    'unmarknsfw':          'api/unmarknsfw/',
    'unmoderated':         'r/{subreddit}/about/unmoderated/',
    'unmute_sender':       'api/unmute_message_author/',
    'unignore_reports':    'api/unignore_reports/',
    'unread':              'message/unread/',
    'unread_message':      'api/unread_message/',
    'unsave':              'api/unsave/',
    'upload_image':        'api/upload_sr_img',
    'user':                'user/{user}/',
    'user_about':          'user/{user}/about/',
    'username_available':  'api/username_available/',
    'vote':                'api/vote/',
    'wiki_edit':           'api/wiki/edit/',
    'wiki_page':           'r/{subreddit}/wiki/{page}',
    'wiki_page_editor':    'r/{subreddit}/api/wiki/alloweditor/{method}',
    'wiki_page_settings':  'r/{subreddit}/wiki/settings/{page}',
    'wiki_pages':          'r/{subreddit}/wiki/pages/',
    'wikibanned':          'r/{subreddit}/about/wikibanned/',
    'wikicontributor':     'r/{subreddit}/about/wikicontributors/'}

JPEG_HEADER = b'\xff\xd8\xff'
MAX_IMAGE_SIZE = 512000
MIN_PNG_SIZE = 67
MIN_JPEG_SIZE = 128
PNG_HEADER = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

USER_AGENT_FORMAT = '{{}} PRAW/{}'.format(__version__)
