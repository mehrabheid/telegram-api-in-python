import os, re
import advertools as adv
from datetime import datetime
from telethon import TelegramClient
from telethon.sync import TelegramClient


# this functions use to get all messages in a telegram channel

def get_messages_in_channel(telegram_channel_name:str):

    channel_name=telegram_channel_name
    telegram_session_path='/where/telegram_session/execute/and/use/telegramSession'

    with TelegramClient(telegram_session_path,'your_telegram_api_id', 'your_telegram_api_hash') as client:
        client:TelegramClient
        client.start('your_telegram_phone_number')
        return client.loop.run_until_complete(Download(client,channel_name))

async def Download(client:TelegramClient, channel_name:str):

    media_dir = '/where/telegram/media/saved'
    path = media_dir
    try: 
        #if path not executed
        os.mkdir(path)
        print("Directory '% s' created" % media_dir) 
    except OSError as error: 
        print(error)


    # save data (messages/media)
    async for message in client.iter_messages(channel_name):
        a = str(message)
        b = a.replace('), ', ')-*-')
        x = b.split('-*-')
        x_channel_Id="".join(x[0])
        result_channel_Id = re.sub('Message\(id\=.*?channel_id=','',x_channel_Id, flags=re.DOTALL)
        result_channel_Id2= re.sub("\)", "", result_channel_Id)
        result_channel_Id3=re.sub("PeerChannel\(channel_id\=", "", result_channel_Id2)
        if "MessageService" in result_channel_Id3:
            result_channel_Id3="MessageService"
        x_Forward_from_channel_Id="".join(x[2])
        if ("fwd_from" not in x_Forward_from_channel_Id):
            x_Forward_from_channel_Id1="".join(x[3])
            if ("fwd_from" not in x_Forward_from_channel_Id1) :
                result_fwd_from2=None  
            else:
                x_fwd_from1="".join(x[3])
                if "MessageFwdHeader" in x_fwd_from1:
                    result_fwd_from1 = re.sub('fwd_from\=MessageFwdHeader\(date\=datetime.datetime\(','',x_fwd_from1, flags=re.DOTALL)
                    result_fwd_from2= re.sub("\,\ tzinfo\=datetime\.timezone\.utc\)", "", result_fwd_from1)
                elif "fwd_from=None" in x_fwd_from1:
                    result_fwd_from2=None    
                else:
                    result_fwd_from2 = re.sub('message\=.*?date\=datetime\.datetime\(','',x_fwd_from1, flags=re.DOTALL)
                    result_fwd_from2= re.sub("\,\ tzinfo\=datetime\.timezone\.utc\)", "", result_fwd_from2)    
            if "MessageService" in result_channel_Id3:
                result_fwd_from2=None
        elif ("fwd_from" in x_Forward_from_channel_Id):
            if ("fwd_from=None" in x_Forward_from_channel_Id) :
                result_fwd_from2=None  
            else:
                x_fwd_from1="".join(x[2])
                if "MessageFwdHeader" in x_fwd_from1:
                    result_fwd_from1 = re.sub('fwd_from\=MessageFwdHeader\(date\=datetime.datetime\(','',x_fwd_from1, flags=re.DOTALL)
                    result_fwd_from1 = re.sub('message\=.*?from_id\=.*?','',result_fwd_from1, flags=re.DOTALL)
                    result_fwd_from1 = result_fwd_from1[result_fwd_from1.find('2'):]
                    result_fwd_from2= re.sub("\,\ tzinfo\=datetime\.timezone\.utc\)", "", result_fwd_from1)

                else:
                    result_fwd_from2 = re.sub('message\=.*?date\=datetime\.datetime\(','',x_fwd_from1, flags=re.DOTALL)
                    result_fwd_from2= re.sub("\,\ tzinfo\=datetime\.timezone\.utc\)", "", result_fwd_from2)
            if "MessageService" in result_channel_Id3:
                result_fwd_from2=None

        text= message.text 
        if "MessageService" in result_channel_Id3 or text == "":
            text=""    
        else:
            emoji_summary = adv.extract_emoji(text)
            try:
                if emoji_summary['emoji'] ==[[]] :
                    pass  
                else:
                    texttt=emoji_summary['emoji']
                for tex in texttt:
                    for t in tex:
                        text=text.replace(t, '')    
            except:
                pass

        #if emojies in message    
        emoji_pattern = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u"\U00002500-\U00002BEF"  # chinese char
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                u"\U0001f926-\U0001f937"
                u"\U00010000-\U0010ffff"
                u"\u2640-\u2642"
                u"\u2600-\u2B55"
                u"\u200d"
                u"\u23cf"
                u"\u23e9"
                u"\u231a"
                u"\ufe0f"  # dingbats
                u"\u3030"
                "]+", flags=re.UNICODE)
        text = emoji_pattern.sub(r'',text)                                                 
        if message.grouped_id != None:
            grouped_id=message.grouped_id
        else:
            grouped_id=0

        if result_fwd_from2==None:
            Forward_from_channel_Id2="None"
        else:    
            x_Forward_from_channel_Id="".join(x[2])

            if ("PeerChannel" not in x_Forward_from_channel_Id):
                x_Forward_from_channel_Id1="".join(x[3])

                if ("PeerChannel" not in x_Forward_from_channel_Id1):
                    x_Forward_from_channel_Id2="".join(x[4])

                    if ("PeerChannel" in x_Forward_from_channel_Id2):
                        x_Forward_from_channel_Id2 = x_Forward_from_channel_Id2[x_Forward_from_channel_Id2.find('channel_id'):]
                        x_Forward_from_channel_Id2 = re.sub('channel_id\=','',x_Forward_from_channel_Id2, flags=re.DOTALL)
                        Forward_from_channel_Id2= re.sub("\)", "", x_Forward_from_channel_Id2)

                    else:
                        Forward_from_channel_Id2= None   

                else:    
                    x_Forward_from_channel_Id1 = x_Forward_from_channel_Id1[x_Forward_from_channel_Id1.find('channel_id'):]
                    x_Forward_from_channel_Id1 = re.sub('channel_id\=','',x_Forward_from_channel_Id1, flags=re.DOTALL)
                    Forward_from_channel_Id2= re.sub("\)", "", x_Forward_from_channel_Id1)

            else:    
                x_Forward_from_channel_Id = x_Forward_from_channel_Id[x_Forward_from_channel_Id.find('channel_id'):]
                x_Forward_from_channel_Id = re.sub('channel_id\=','',x_Forward_from_channel_Id, flags=re.DOTALL)
                Forward_from_channel_Id2= re.sub("\)", "", x_Forward_from_channel_Id)    

        if "MessageService" in result_channel_Id3:
            Forward_from_channel_Id2=""        
        author=message.post_author
        try :

            if result_fwd_from2==None:
                result_x_Post_author2 = None 
            else:    
                x_Post_author="".join(x[2])
                if ("post_author" not in x_Post_author):
                    x_Post_author1="".join(x[3])

                    if ("post_author" not in x_Post_author1):
                        x_Post_author2="".join(x[4])
                        if ("post_author" in x_Post_author2):
                            result_x_Post_author1 = re.sub('from_name\=.*?\,\ channel_post\=.*?\,\ post_author\=\'','',x_Post_author2, flags=re.DOTALL)
                            result_x_Post_author2= re.sub('\'\,\ saved_from_peer\=.*?\,\ saved_from_msg_id\=.*?\,\ psa_type\=.*?\)', '', result_x_Post_author1)
                            if "channel_post" in result_x_Post_author2:
                                result_x_Post_author2 = None
                            if "ttl_period" in result_x_Post_author2:
                                result_x_Post_author2 = None
                        else:
                            result_x_Post_author2 = None
                    else:
                        result_x_Post_author1 = re.sub('from_name\=.*?\,\ channel_post\=.*?\,\ post_author\=\'','',x_Post_author1, flags=re.DOTALL)
                        result_x_Post_author2= re.sub('\'\,\ saved_from_peer\=.*?\,\ saved_from_msg_id\=.*?\,\ psa_type\=.*?\)', '', result_x_Post_author1)
                        if "channel_post" in result_x_Post_author2:
                            result_x_Post_author2 = None
                        if "ttl_period" in result_x_Post_author2:
                            result_x_Post_author2 = None        
                else:
                    result_x_Post_author1 = re.sub('from_name\=.*?\,\ channel_post\=.*?\,\ post_author\=\'','',x_Post_author, flags=re.DOTALL)
                    result_x_Post_author2= re.sub('\'\,\ saved_from_peer\=.*?\,\ saved_from_msg_id\=.*?\,\ psa_type\=.*?\)', '', result_x_Post_author1)
                    if "channel_post" in result_x_Post_author2:
                        result_x_Post_author2 = None
                    if "ttl_period" in result_x_Post_author2:
                        result_x_Post_author2 = None
        except:
            result_x_Post_author2 = None 

        if (result_fwd_from2 == None) or ("MessageService" in result_channel_Id3):
            forwarded=0
        else:
            forwarded=1    
        if message.pinned ==True:
            pin=1
        elif message.pinned ==False:
            pin=0
        else:
            pin=0 


        directory = result_channel_Id3
        media_dir = '/your/media/directory'
        path2 = os.path.join(media_dir,directory)
        try: 
            os.mkdir(path2)
        except OSError as error: 
            print('media saved successfully')

        # save media
        if message.file :
            path = await message.download_media(media_dir + "/" + result_channel_Id3)

            if '\\' in path:
                path= path.replace("\\", "/")
        else :
            path = ""


        
        sqlquery="INSERT INTO telegram_messages (Channel_id,message_id,message_date,forward_date,message_txt,path,media_group_id,forward_from_channel_id,message_author,forward_post_author,forward_bool,pinned_bool) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sqlvals=(result_channel_Id3,message.id,message.date,result_fwd_from2,text,path,grouped_id,Forward_from_channel_Id2,author,result_x_Post_author2,forwarded,pin,)
        # execute query & commit connection (sqlquery,sqlvals) to save in your database

    print("History Finished Successfuly")    
    return 



get_messages_in_channel('https://t.me/username')
