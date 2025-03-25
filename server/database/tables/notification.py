from .needed import *


# while thinking about notification system
# i caught myself thinking that it's not very cool 
# to send a notification with pre-prepared content. 
# In case the client application will support multiple languages ​
# have prepared notification content for each seems overkill.
# 
# SO GOODLUCK TO FUTURE ME TO PARSE THIS SHIT IN JAVASCRIPT
# 
# notification syntax
# {type: String, arguments: [...]}
# possible values: 
# Type                    Arguments
# NewPages                [TitleId, PageId]
# PersonApproved          [PersonId]
# PersonDeclined          []
# TitleApproved           [TitleId]
# TitleDeclined           []
# CommentIsHyping         [CommentId]
# RoleChange              [Muted|Default|Moderator|Admin]
# PendingTitleChanges     [TitleId]
# PendingTitle            [TitleMetaId]
# PendingPersonChanges    [PersonId]
# PendingPerson           [PersonMetaId]

class Notification(Base):
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True)
    user_uuid = Column(String, ForeignKey('user.uuid'))
    
    type = Column(String)
    # string splitted by "/" to containt multiple arguments at once
    arguments = Column(String)
    viewed = Column(Boolean) 

    timestamp = Column(Integer, nullable=False)


class TitlePageSubscription(Base):
    """
    Table of users subscribed to title updates.
    Needed to notify subscribed users each time new pages is approved.
    """
    __tablename__ = 'title_page_subscription'
    id = Column(Integer, primary_key=True)
    title_id = Column(Integer, ForeignKey('title.id'))
    user_uuid = Column(String, ForeignKey('user.uuid'))