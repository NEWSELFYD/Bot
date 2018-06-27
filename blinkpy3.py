from linepy import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz,tweepy, urllib, urllib.parse, wikipedia, atexit, datetime
from gtts import gTTS
from googletrans import Translator
#==============================================================================================================
botStart = time.time()
#==============================================================================================================
client = LINE()
#client = LINE("TOKENMU")
#client = LINE("Email","Password")
client.log("Auth Token : " + str(client.authToken))
channelToken = client.getChannelResult()
client.log("Channel Token : " + str(channelToken))
#==============================================================================================================
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
#==============================================================================================================
mid = client.getProfile().mid
#==============================
clientMID = client.profile.mid
#==============================
clientProfile = client.getProfile()
#==============================================================================================================
clientSettings = client.getSettings()
#==============================================================================================================
oepoll = OEPoll(client)
#==============================================================================================================
admin = "MID KAMU"
#==============================================================================================================
Bots=[mid]
#==============================================================================================================
contact = client.getProfile()
backup = client.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
#==============================================================================================================
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}
cctv = {
  "point":{},
  "cyduk":{},
  "sidermem":{}
}
#==============================================================================================================
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
#==============================================================================================================
myProfile["displayName"] = clientProfile.displayName
myProfile["statusMessage"] = clientProfile.statusMessage
myProfile["pictureStatus"] = clientProfile.pictureStatus
#==============================================================================================================
read = json.load(readOpen)
settings = json.load(settingsOpen)
#==============================================================================================================
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Rh'
        client.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
#==============================================================================================================
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
#==============================================================================================================
def logError(text):
    client.log("[ INFO ] ERROR : " + str(text))
    time_ = datetime.datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time_), text))
#==============================================================================================================
def delete_log():
    ndt = datetime.datetime.now()
    for data in msg_dict:
        if (datetime.datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
#==============================================================================================================
def command(text):
    pesan = text.lower()
    if pesan.startswith(settings["keyCommand"]):
        cmd = pesan.replace(settings["keyCommand"],"")
    else:
        cmd = "Undefined command"
    return cmd
#==============================================================================================================
def help():
    key = settings["keyCommand"]
    key = key.title()
    helpMessage = "" + "               •♬「 Blink bot 」\n" + \
	                "" + "•♬ Gunakan ➢ 「 " + key + " 」" + "\n" + \
                  "" + "•♬ " + key + "tts" + "\n" + \
                  "" + "•♬ " + key + "translate" + "\n" + \
                  "" + "•♬ " + key + "About" + "\n" + \
                  "" + "•♬ " + key + "Mention" + "\n" + \
                  "" + "•♬ " + key + "Restart" + "\n" + \
                  "" + "•♬ " + key + "Runtime" + "\n" + \
                  "" + "•♬ " + key + "Me" + "\n" + \
                  "" + "•♬ " + key + "Gift" + "\n" + \
                  "" + "•♬ " + key + "Cpp" + "\n" + \
                  "" + "•♬ " + key + "Myname: 「text」" + "\n" + \
                  "" + "•♬ " + key + "Mybio: 「text」" + "\n" + \
                  "" + "•♬ " + key + "Cgp" + "\n" + \
                  "" + "•♬ " + key + "Vkick 「@」" + "\n" + \
                  "" + "•♬ " + key + "Kick 「@」" + "\n" + \
                  "" + "•♬ " + key + "A1fuck 「@」" + "\n" + \
                  "" + "•♬ " + key + "Mid" + "\n" + \
                  "" + "•♬ " + key + "Myname" + "\n" + \
                  "" + "•♬ " + key + "Mybio" + "\n" + \
                  "" + "•♬ " + key + "Mypic" + "\n" + \
                  "" + "•♬ " + key + "Myvid" + "\n" + \
                  "" + "•♬ " + key + "Mycover" + "\n" + \
                  "" + "•♬ " + key + "Getmid/「@」" + "\n" + \
                  "" + "•♬ " + key + "Getcontact/「@」" + "\n" + \
                  "" + "•♬ " + key + "Getname/「@」" + "\n" + \
                  "" + "•♬ " + key + "Getbio/「@」" + "\n" + \
                  "" + "•♬ " + key + "Getpic/「@」" + "\n" + \
                  "" + "•♬ " + key + "Getvid/「@」" + "\n" + \
                  "" + "•♬ " + key + "Getcover/「@」" + "\n" + \
                  "" + "•♬ " + key + "Getid/「@」" + "\n" + \
                  "" + "•♬ " + key + "GetPicAll" + "\n" + \
                  "" + "•♬ " + key + "GetPicGroup" + "\n" + \
                  "" + "•♬ " + key + "GetPic 「FriendName」" + "\n" + \
                  "" + "•♬ " + key + "GetPicGroup 「GroupName」" + "\n" + \
                  "" + "•♬ " + key + "Clone 「@」" + "\n" + \
                  "" + "•♬ " + key + "CloneCover 「@」" + "\n" + \
                  "" + "•♬ " + key + "Restore" + "\n" + \
                  "" + "•♬ " + key + "Spam on 「Numb」 「Text」" + "\n" + \
                  "" + "•♬ " + key + "Stag 「Numb」 「@」" + "\n" + \
                  "" + "•♬ " + key + "Tag 「Numb」" + "\n" + \
                  "" + "•♬ " + key + "Stickers" + "\n" + \
                  "" + "•♬ " + key + "SpamStickers 「Numb」 「Key」" + "\n" + \
                  "" + "•♬ " + key + "Gcast 「Text」" + "\n" + \
                  "" + "•♬ " + key + "Pmcast 「Text」" + "\n" + \
                  "" + "•♬ " + key + "Leave 「GroupName」" + "\n" + \
                  "" + "•♬ " + key + "Kalender" + "\n" + \
                  "" + "•♬ " + key + "Speed" + "\n" + \
                  "" + "•♬ " + key + "Clearchat" + "\n" + \
                  "" + "•♬ " + key + "Leave" + "\n" + \
                  "" + "•♬ " + key + "Gcreator" + "\n" + \
                  "" + "•♬ " + key + "Ginfo" + "\n" + \
                  "" + "•♬ " + key + "MemberList" + "\n" + \
                  "" + "•♬ " + key + "GroupList" + "\n" + \
                  "" + "•♬ " + key + "FriendList" + "\n" + \
                  "" + "•♬ " + key + "BlockList" + "\n" + \
                  "" + "•♬ " + key + "BanList" + "\n" + \
                  "" + "•♬ " + key + "AuthorList" + "\n" + \
                  "" + "•♬ " + key + "Gn 「NewGroupName」" + "\n" + \
                  "" + "•♬ " + key + "Url" + "\n" + \
                  "" + "•♬ " + key + "Curl" + "\n" + \
                  "" + "•♬ " + key + "Lurking on/off" + "\n" + \
                  "" + "•♬ " + key + "Lurking result" + "\n" + \
                  "" + "•♬ " + key + "Sider:on/off" + "\n" + \
                  "" + "•♬ " + key + "Set" + "\n" + \
                  "" + "•♬ " + key + "Qrjoin on/off" + "\n" + \
                  "" + "•♬ " + key + "Protect on/off" + "\n" + \
                  "" + "•♬ " + key + "Cancel on/off" + "\n" + \
                  "" + "•♬ " + key + "Invite on/off" + "\n" + \
                  "" + "•♬ " + key + "Qr on/off" + "\n" + \
                  "" + "•♬ " + key + "Dc on/off" + "\n" + \
                  "" + "•♬ " + key + "Autojoin author/off" + "\n" + \
                  "" + "•♬ " + key + "AutoLeave on/off" + "\n" + \
                  "" + "•♬ " + key + "AutoRead on/off" + "\n" + \
                  "" + "•♬ " + key + "AutoLeave on/off" + "\n" + \
                  "" + "•♬ " + key + "Mimic on/off" + "\n" + \
                  "" + "•♬ " + key + "Mimicadd/del 「@」" + "\n" + \
                  "" + "•♬ " + key + "Mimiclist" + "\n" + \
                  "" + "•♬ " + key + "SS 「Link」" + "\n" + \
                  "" + "•♬ " + key + "Igpost 「Username」" + "\n" + \
                  "" + "•♬ " + key + "Ig 「Username」" + "\n" + \
                  "" + "•♬ " + key + "Getimage 「Query」" + "\n" + \
                  "" + "•♬ " + key + "Wikipedia 「Query」" + "\n" + \
                  "" + "•♬ " + key + "CheckPrayTime 「Location」" + "\n" + \
                  "" + "•♬ " + key + "CheckWeather 「Location」" + "\n" + \
                  "" + "•♬ " + key + "CheckLocation 「Location」" + "\n" + \
                  "" + "•♬ " + key + "Getmusic 「Query」" + "\n" + \
                  "" + "•♬ " + key + "Getlyric 「Query」" + "\n" + \
                  "" + "•♬ " + key + "Getyt 「Query」" + "\n" + \
                  "" + "•♬ " + key + "Getvideo 「Query」" + "\n" + \
                  "" + "•♬ " + key + "Imagetext 「Text」" + "\n" + \
                  "" + "•♬ " + key + "Ban:on/「@」" + "\n" + \
                  "" + "•♬ " + key + "Unban:on/「@」" + "\n" + \
                  "" + "•♬ " + key + "Blc" + "\n" + \
                  "" + "•♬ " + key + "Clearban" + "\n"
    return helpMessage
#==============================================================================================================
def helptexttospeech():
    key = settings["keyCommand"]
    key = key.title()
    texttospeech = "" + "╔══[ T E X T   T O   S P E E C H ]" + "\n" + \
                   "" + "╠" + key + " af : Afrikaans" + "\n" + \
                   "" + "╠" + key + " sq : Albanian" + "\n" + \
                   "" + "╠" + key + " ar : Arabic" + "\n" + \
                   "" + "╠" + key + " hy : Armenian" + "\n" + \
                   "" + "╠" + key + " bn : Bengali" + "\n" + \
                   "" + "╠" + key + " ca : Catalan" + "\n" + \
                   "" + "╠" + key + " zh : Chinese" + "\n" + \
                   "" + "╠" + key + " zh-cn : Chinese (Mandarin/China)" + "\n" + \
                   "" + "╠" + key + " zh-tw : Chinese (Mandarin/Taiwan)" + "\n" + \
                   "" + "╠" + key + " zh-yue : Chinese (Cantonese)" + "\n" + \
                   "" + "╠" + key + " hr : Croatian" + "\n" + \
                   "" + "╠" + key + " cs : Czech" + "\n" + \
                   "" + "╠" + key + " da : Danish" + "\n" + \
                   "" + "╠" + key + " nl : Dutch" + "\n" + \
                   "" + "╠" + key + " en : English" + "\n" + \
                   "" + "╠" + key + " en-au : English (Australia)" + "\n" + \
                   "" + "╠" + key + " en-uk : English (United Kingdom)" + "\n" + \
                   "" + "╠" + key + " en-us : English (United States)" + "\n" + \
                   "" + "╠" + key + " eo : Esperanto" + "\n" + \
                   "" + "╠" + key + " fi : Finnish" + "\n" + \
                   "" + "╠" + key + " fr : French" + "\n" + \
                   "" + "╠" + key + " de : German" + "\n" + \
                   "" + "╠" + key + " el : Greek" + "\n" + \
                   "" + "╠" + key + " hi : Hindi" + "\n" + \
                   "" + "╠" + key + " hu : Hungarian" + "\n" + \
                   "" + "╠" + key + " is : Icelandic" + "\n" + \
                   "" + "╠" + key + " id : Indonesian" + "\n" + \
                   "" + "╠" + key + " it : Italian" + "\n" + \
                   "" + "╠" + key + " ja : Japanese" + "\n" + \
                   "" + "╠" + key + " km : Khmer (Cambodian)" + "\n" + \
                   "" + "╠" + key + " ko : Korean" + "\n" + \
                   "" + "╠" + key + " la : Latin" + "\n" + \
                   "" + "╠" + key + " lv : Latvian" + "\n" + \
                   "" + "╠" + key + " mk : Macedonian" + "\n" + \
                   "" + "╠" + key + " no : Norwegian" + "\n" + \
                   "" + "╠" + key + " pl : Polish" + "\n" + \
                   "" + "╠" + key + " pt : Portuguese" + "\n" + \
                   "" + "╠" + key + " ro : Romanian" + "\n" + \
                   "" + "╠" + key + " ru : Russian" + "\n" + \
                   "" + "╠" + key + " sr : Serbian" + "\n" + \
                   "" + "╠" + key + " si : Sinhala" + "\n" + \
                   "" + "╠" + key + " sk : Slovak" + "\n" + \
                   "" + "╠" + key + " es : Spanish" + "\n" + \
                   "" + "╠" + key + " es-es : Spanish (Spain)" + "\n" + \
                   "" + "╠" + key + " es-us : Spanish (United States)" + "\n" + \
                   "" + "╠" + key + " sw : Swahili" + "\n" + \
                   "" + "╠" + key + " sv : Swedish" + "\n" + \
                   "" + "╠" + key + " ta : Tamil" + "\n" + \
                   "" + "╠" + key + " th : Thai" + "\n" + \
                   "" + "╠" + key + " tr : Turkish" + "\n" + \
                   "" + "╠" + key + " uk : Ukrainian" + "\n" + \
                   "" + "╠" + key + " vi : Vietnamese" + "\n" + \
                   "" + "╠" + key + " cy : Welsh" + "\n" + \
                   "" + "╚══[ Example : Say-id Gue Gans! ]" + "\n" + "" + \
                   ""
    return texttospeech
    
def helptranslate():
    key = settings["keyCommand"]
    key = key.title()
    helpTranslate ="" + "╔══[ T R A N S L A T E ]" + "\n" + \
                   "" + "╠" + key + " af : Afrikaans" + "\n" + \
                   "" + "╠" + key + " sq : Albanian" + "\n" + \
                   "" + "╠" + key + " ar : Arabic" + "\n" + \
                   "" + "╠" + key + " hy : Armenian" + "\n" + \
                   "" + "╠" + key + " bn : Bengali" + "\n" + \
                   "" + "╠" + key + " ca : Catalan" + "\n" + \
                   "" + "╠" + key + " zh : Chinese" + "\n" + \
                   "" + "╠" + key + " zh-cn : Chinese (Mandarin/China)" + "\n" + \
                   "" + "╠" + key + " zh-tw : Chinese (Mandarin/Taiwan)" + "\n" + \
                   "" + "╠" + key + " zh-yue : Chinese (Cantonese)" + "\n" + \
                   "" + "╠" + key + " hr : Croatian" + "\n" + \
                   "" + "╠" + key + " cs : Czech" + "\n" + \
                   "" + "╠" + key + " da : Danish" + "\n" + \
                   "" + "╠" + key + " nl : Dutch" + "\n" + \
                   "" + "╠" + key + " en : English" + "\n" + \
                   "" + "╠" + key + " en-au : English (Australia)" + "\n" + \
                   "" + "╠" + key + " en-uk : English (United Kingdom)" + "\n" + \
                   "" + "╠" + key + " en-us : English (United States)" + "\n" + \
                   "" + "╠" + key + " eo : Esperanto" + "\n" + \
                   "" + "╠" + key + " fi : Finnish" + "\n" + \
                   "" + "╠" + key + " fr : French" + "\n" + \
                   "" + "╠" + key + " de : German" + "\n" + \
                   "" + "╠" + key + " el : Greek" + "\n" + \
                   "" + "╠" + key + " hi : Hindi" + "\n" + \
                   "" + "╠" + key + " hu : Hungarian" + "\n" + \
                   "" + "╠" + key + " is : Icelandic" + "\n" + \
                   "" + "╠" + key + " id : Indonesian" + "\n" + \
                   "" + "╠" + key + " it : Italian" + "\n" + \
                   "" + "╠" + key + " ja : Japanese" + "\n" + \
                   "" + "╠" + key + " km : Khmer (Cambodian)" + "\n" + \
                   "" + "╠" + key + " ko : Korean" + "\n" + \
                   "" + "╠" + key + " la : Latin" + "\n" + \
                   "" + "╠" + key + " lv : Latvian" + "\n" + \
                   "" + "╠" + key + " mk : Macedonian" + "\n" + \
                   "" + "╠" + key + " no : Norwegian" + "\n" + \
                   "" + "╠" + key + " pl : Polish" + "\n" + \
                   "" + "╠" + key + " pt : Portuguese" + "\n" + \
                   "" + "╠" + key + " ro : Romanian" + "\n" + \
                   "" + "╠" + key + " ru : Russian" + "\n" + \
                   "" + "╠" + key + " sr : Serbian" + "\n" + \
                   "" + "╠" + key + " si : Sinhala" + "\n" + \
                   "" + "╠" + key + " sk : Slovak" + "\n" + \
                   "" + "╠" + key + " es : Spanish" + "\n" + \
                   "" + "╠" + key + " es-es : Spanish (Spain)" + "\n" + \
                   "" + "╠" + key + " es-us : Spanish (United States)" + "\n" + \
                   "" + "╠" + key + " sw : Swahili" + "\n" + \
                   "" + "╠" + key + " sv : Swedish" + "\n" + \
                   "" + "╠" + key + " ta : Tamil" + "\n" + \
                   "" + "╠" + key + " th : Thai" + "\n" + \
                   "" + "╠" + key + " tr : Turkish" + "\n" + \
                   "" + "╠" + key + " uk : Ukrainian" + "\n" + \
                   "" + "╠" + key + " vi : Vietnamese" + "\n" + \
                   "" + "╠" + key + " cy : Welsh" + "\n" + \
                   "" + "╚══[ Example : tr-id i'm handsome ]" + "\n" + "" + \
                   ""
    return helpTranslate
#==============================================================================================================
#=============================================[ OPERATION STARTED ]============================================
#==============================================================================================================
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                client.sendMessage(op.param1, "Halo {} terimakasih telah menambahkan saya sebagai teman :D".format(str(client.getContact(op.param1).displayName)))
#==============================================================================================================
#==============================================[OP TYPE 13 JOIN]===============================================
#==============================================================================================================
        if op.type == 13:
            if mid in op.param3:
                group = client.getGroup(op.param1)
                contact = client.getContact(op.param2)
                if settings["autoJoin"] == True:
                    client.acceptGroupInvitation(op.param1)
#==============================================================================================================
        if op.type == 11:
            if settings["qrp"] == True:
                if op.param2 in Bots:
                    pass
                else:
                    try:
                        group = client.getGroup(op.param1)
                        group.preventedJoinByTicket = True
                        Ticket = assist.reissueGroupTicket(op.param1)
                        assist3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        assist3.kickoutFromGroup(op.param1,[op.param2])
                        assist3.sendMessage(op.param1, text=None, contentMetadata={'mid': op.param2}, contentType=13)
                        group = assist2.getGroup(op.param1)
                        group.preventedJoinByTicket = True
                        assist2.updateGroup(group)
                        assist3.leaveGroup(op.param1)
                        settings["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    except:
                        pass
        if op.type == 13:
            if settings["pinvite"] == True:
                if op.param2 in Bots:
                    pass
                else:
                    try:
                        group = client.getGroup(op.param1)
                        group.preventedJoinByTicket = True
                        Ticket = assist.reissueGroupTicket(op.param1)
                        assist3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        assist3.kickoutFromGroup(op.param1,[op.param2])
                        assist3.sendMessage(op.param1, text=None, contentMetadata={'mid': op.param2}, contentType=13)
                        group = assist2.getGroup(op.param1)
                        group.preventedJoinByTicket = True
                        assist2.updateGroup(group)
                        assist3.leaveGroup(op.param1)
                        settings["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    except:
                        pass
#==============================================================================================================
        if op.type == 19:
            if settings["protect"] == True:
                if op.param2 in Bots:
                    pass
                else:
                    try:
                        group = client.getGroup(op.param1)
                        group.preventedJoinByTicket = True
                        Ticket = assist.reissueGroupTicket(op.param1)
                        assist3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        assist3.kickoutFromGroup(op.param1,[op.param2])
                        assist3.sendMessage(op.param1, text=None, contentMetadata={'mid': op.param2}, contentType=13)
                        group = assist2.getGroup(op.param1)
                        group.preventedJoinByTicket = True
                        assist2.updateGroup(group)
                        assist3.leaveGroup(op.param1)
                        settings["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    except:
                        pass
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
#==============================================================================================================
#==============================================[OP TYPE 22 24 JOIN]============================================
#==============================================================================================================
        if op.type == 22:
            if settings["autoLeave"] == True:
                client.leaveRoom(op.param1)
        if op.type == 24:
            if settings["autoLeave"] == True:
                client.leaveRoom(op.param1)
#==============================================================================================================
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != client.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == "mykey" or text.lower() == "key" or text.lower() == "setkey":
                    client.sendMessage(msg.to, "「 ", " 」\nYourkey Is: 「 " + str(settings["keyCommand"]) + " 」")
                elif msg.text.lower().startswith("setkey "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    settings["keyCommand"] = str(say).lower()
                    client.sendMessage(msg.to, "「 ", " 」\nYourkey set to 「 " + str(settings["keyCommand"]) + " 」")   #                 kicker2.sendMessage(to, (say))
#==============================================================================================================
                elif text.lower() == "koran" or text.lower() == "help":
                    helpMessage = help()
                    client.sendMessage(to, str(helpMessage))
                elif msg.text.lower().startswith("contact "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    client.sendMessage(receiver, None, contentMetadata={'mid': say}, contentType=13)
#==============================================================================================================
                elif msg.text.lower() == "." or msg.text.lower() == "@join":
                    X = client.getGroup(to)
                    X.preventedJoinByTicket = False
                    client.updateGroup(X)
                    invsend = 0
                    Ti = client.reissueGroupTicket(to)
                    assist1.acceptGroupInvitationByTicket(to,Ti)
                    assist2.acceptGroupInvitationByTicket(to,Ti)
                    G = assist1.getGroup(to)
                    G.preventedJoinByTicket = True
                    assist1.updateGroup(G)
                elif msg.text.lower() == "bots siriqr" or msg.text.lower() == "siriqr":
                    X = assist1.getGroup(to)
                    X.preventedJoinByTicket = False
                    assist1.updateGroup(X)
                    invsend = 0
                    Ti = assist1.reissueGroupTicket(to)
                    assist3.acceptGroupInvitationByTicket(to,Ti)
                    G = assist1.getGroup(to)
                    G.preventedJoinByTicket = True
                    assist1.updateGroup(G)
                elif msg.text.lower() == "," or msg.text.lower() == "@bye":
                    if msg.toType == 2:
                        ginfo = client.getGroup(to)
                        try:
                            assist1.sendMessage(to, "Bye bye {} ♪".format(str(ginfo.name)))
                            assist1.leaveGroup(to)
                            assist2.leaveGroup(to)
                        except:
                            pass
                elif msg.text.lower() == "siri @bye":
                    if msg.toType == 2:
                        ginfo = client.getGroup(to)
                        try:
                            assist3.leaveGroup(to)
                        except:
                            pass
#==============================================================================================================
#==============================================================================================================
#==============================================================================================================
                elif "Kick " in msg.text:
                    if msg._from in clientMID:                                                                                                                                       
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]                                                                                                                                
                        targets = []
                        for x in key["MENTIONEES"]:                                                                                                                                  
                            targets.append(x["M"])
                        for target in targets:                                                                                                                                       
                            try:
                                client.kickoutFromGroup(msg.to,[target])
                            except:
                                pass
                elif "Vkick " in msg.text:
                    if msg._from in clientMID:                                                                                                                                       
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]                                                                                                                                
                        targets = []
                        for x in key["MENTIONEES"]:                                                                                                                                  
                            targets.append(x["M"])
                        for target in targets:                                                                                                                                       
                            try:
                                client.kickoutFromGroup(msg.to,[target])
                                client.inviteIntoGroup(msg.to,[target])
                                client.cancelGroupInvitation(msg.to,[target])
                            except:
                                pass
                elif "A1fuck " in msg.text:
                    if msg._from in clientMID:                                                                                                                                       
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]                                                                                                                                
                        targets = []
                        for x in key["MENTIONEES"]:                                                                                                                                  
                            targets.append(x["M"])
                        for target in targets:                                                                                                                                       
                            try:
                                assist1.kickoutFromGroup(msg.to,[target])
                            except:
                                pass
                elif "A2fuck " in msg.text:
                    if msg._from in clientMID:                                                                                                                                       
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]                                                                                                                                
                        targets = []
                        for x in key["MENTIONEES"]:                                                                                                                                  
                            targets.append(x["M"])
                        for target in targets:                                                                                                                                       
                            try:
                                assist2.kickoutFromGroup(msg.to,[target])
                            except:
                                pass
                elif "A3kickinv " in msg.text:
                    if msg._from in clientMID:                                                                                                                                       
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]                                                                                                                                
                        targets = []
                        for x in key["MENTIONEES"]:                                                                                                                                  
                            targets.append(x["M"])
                        for target in targets:                                                                                                                                       
                            try:
                                group = client.getGroup(msg.to)
                                group.preventedJoinByTicket = False
                                client.updateGroup(group)
                                Ticket = client.reissueGroupTicket(msg.to)
                                assist3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                assist3.kickoutFromGroup(msg.to,[target])
                                assist3.findAndAddContactsByMid(target)
                                assist3.inviteIntoGroup(msg.to,[target])
                                assist3.sendMessage(msg.to, text=None, contentMetadata={'mid': target}, contentType=13)
                                group = assist3.getGroup(msg.to)
                                group.preventedJoinByTicket = True
                                assist3.updateGroup(group)
                                assist3.leaveGroup(msg.to)
                            except:
                                pass
                elif "A3inv " in msg.text:
                    if msg._from in clientMID:                                                                                                                                       
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]                                                                                                                                
                        targets = []
                        for x in key["MENTIONEES"]:                                                                                                                                  
                            targets.append(x["M"])
                        for target in targets:                                                                                                                                       
                            try:
                                group = client.getGroup(msg.to)
                                group.preventedJoinByTicket = False
                                client.updateGroup(group)
                                Ticket = client.reissueGroupTicket(msg.to)
                                assist3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                assist3.findAndAddContactsByMid(target)
                                assist3.inviteIntoGroup(msg.to,[target])
                                assist3.sendMessage(msg.to, text=None, contentMetadata={'mid': target}, contentType=13)
                                group = assist3.getGroup(msg.to)
                                group.preventedJoinByTicket = True
                                assist3.updateGroup(group)
                                assist3.leaveGroup(msg.to)
                            except:
                                pass
#==============================================================================================================
                elif msg.text.lower().startswith("say-af "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'af'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-sq "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sq'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-ar "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ar'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-hy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-bn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'bn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-ca "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ca'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-zh "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-zh-cn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-cn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-zh-tw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-zh-yue "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-yue'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-hr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-cs "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cs'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-da "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'da'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-nl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'nl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-en "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-en-au "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-au'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-en-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-en-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-eo "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'eo'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-fi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-fr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-de "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'de'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-el "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'el'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-hi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-hu "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hu'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-is "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'is'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-id "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-it "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'it'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-ja "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-km "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'km'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-ko "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ko'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-la "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'la'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-lv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'lv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-mk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'mk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-no "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'no'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-pl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-pt "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pt'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-do "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ro'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-ru "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ru'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-sr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-si "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'si'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-sk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-es-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-es-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-sw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-sv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-ta "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ta'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-th "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-tr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'tr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-vi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'vi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("say-cy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    client.sendAudio(msg.to,"hasil.mp3")
#==============================================================================================================
                elif msg.text.lower().startswith("tr-af "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='af')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sq "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sq')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-am "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='am')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ar "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hy')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-az "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='az')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-eu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='eu')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-be "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='be')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bn')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bs')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bg')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ca "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ca')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ceb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ceb')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ny "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ny')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-cn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-cn')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-tw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-co "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='co')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hr')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cs')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-da "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='da')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-nl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='nl')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-en "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-et "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='et')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fi')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fy')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gl')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ka "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ka')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-de "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-el "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='el')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gu')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ht "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ht')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ha "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ha')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-haw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='haw')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-iw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='iw')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hi')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hmn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hmn')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hu')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-is "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='is')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ig "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ig')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-id "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ga "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ga')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-it "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='it')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ja "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-jw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='jw')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kn')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kk')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-km "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='km')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ko "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ko')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ku "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ku')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ky "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ky')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lo')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-la "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='la')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lv')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lt')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lb')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mk')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mg')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ms "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ms')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ml "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ml')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mt')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mi')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mr')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mn')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-my "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='my')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ne "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ne')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-no "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='no')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ps "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ps')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fa')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pl')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pt')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pa')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ro "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ro')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ru "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ru')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sm "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sm')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gd')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sr')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-st "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='st')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sn')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sd')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-si "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='si')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sl')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-so "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='so')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-es "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='es')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-su "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='su')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sw')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sv')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tg')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ta "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ta')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-te "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='te')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tr')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uk')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ur "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ur')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uz "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uz')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-vi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='vi')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cy')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-xh "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='xh')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yi')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yo')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zu')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fil "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fil')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-he "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='he')
                    A = hasil.text
                    client.sendMessage(msg.to, A)
#==============================================================================================================
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
                elif msg.toType == 2:
                    to = receiver
                if settings["autoRead"] == True:
                    client.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 13:
                    if settings["checkContact"] == True:
                        msg.contentType = 0
                        client.sendMessage(msg.to,msg.contentMetadata["mid"])
                        if 'displayName' in msg.contentMetadata:
                            contact = client.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = channel.getProfileCoverURL(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            client.sendMessage(msg.to,"「DisplayName」:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                        else:
                            contact = client.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = channel.getProfileCoverURL(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            if settings["server"] == "VPS":
                                client.sendMessage(msg.to,"「DisplayName」:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                                client.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                                client.sendImageWithURL(msg.to,str(cu))
#==============================================================================================================
#==========================================[ SCRIPT SELF START ]===============================================
#==============================================================================================================
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if settings["autoRead"] == True:
                        client.sendChatChecked(to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                    if cmd != "Undefined command":
#==============================================================================================================
                        if cmd == "tts":
                            texttospeech = helptexttospeech()
                            client.sendMessage(to, str(texttospeech))
                        elif cmd == "translate":
                            helpTranslate = helptranslate()
                            client.sendMessage(to, str(helpTranslate))
                        elif cmd == "restart" or cmd == "reboot":
                            client.sendMessage(to, "Restarted")
                            settings["restartPoint"] = to
                            restartBot()
                        elif cmd == "runtime":
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = format_timespan(runtime)
                            resetTime = timeNow - int(settings["timeRestart"])
                            client.sendMessage(to, "Running time「{}」".format(str(runtime)))
                        elif cmd == "me":
                            contact = client.getContact(clientMID)
                            RhyN_(to, contact.mid)
                            client.sendContact(to, sender)
                        elif cmd == "gift":
                            client.sendMessage(to, text=None, contentMetadata=None, contentType=9)
                        elif cmd == "cpp":
                            settings["changePicture"] = True
                            client.sendMessage(to, "Send Pict!")
                        elif cmd == "cgp":
                            if msg.toType == 2:
                                if to not in settings["changeGroupPicture"]:
                                    settings["changeGroupPicture"].append(to)
                                client.sendMessage(to, "Send Pict!")
                        elif cmd.startswith("myname:"):
                            string = text.replace("myname:","")
                            if len(string.encode('utf-8')) <= 20:
                                profile = client.getProfile()
                                profile.displayName = string
                                client.updateProfile(profile)
                                client.sendMessage(to,"Myname updated to 「 " + string + " 」")
                        elif cmd.startswith("mybio:"):
                            string = text.replace("mybio:","")
                            if len(string.encode('utf-8')) <= 500:
                                profile = client.getProfile()
                                profile.statusMessage = string
                                client.updateProfile(profile)
                                client.sendMessage(to,"Mybio updated to 「 " + string + " 」")
#==============================================================================================================
                        elif cmd == 'mid':
                            client.sendMessage(to, clientMID)
                        elif cmd == 'myname':
                            me = client.getContact(clientMID)
                            client.sendMessage(to,"「 DisplayName 」\n" + me.displayName)
                        elif cmd == 'mybio':
                            me = client.getContact(clientMID)
                            client.sendMessage(to,"「 StatusMessage 」\n" + me.statusMessage)
                        elif cmd == 'mypic':
                            me = client.getContact(mid)
                            client.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                        elif cmd == 'myvid':
                            me = client.getContact(clientMID)
                            client.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                        elif cmd == 'mycover':
                            if client != None:
                                path = client.getProfileCoverURL(clientMID)
                                path = str(path)
                                if settings["server"] == "VPS":
                                    client.sendImageWithURL(to, str(path))
                                else:
                                    urllib.urlretrieve(path, "steal.jpg")
                                    client.sendImage(to, "steal.jpg")
                            else:
                                client.sendMessage(to, "Talk Exception")
                        elif cmd == "clear invite":
                            ginvited = client.getGroupIdsInvited()
                            if ginvited != [] and ginvited != None:
                                for gid in ginvited:
                                    client.rejectGroupInvitation(gid)
                                client.sendMessage(to, "Reject {} Group invitation".format(str(len(ginvited))))
                            else:
                                client.sendMessage(to, "")
#==============================================================================================================
                        elif cmd == 'getmid':
                            client.sendMessage(to,"「 MID 」\n" +  to)
                        elif cmd == 'getcontact':
                            client.sendMessage(to, text=None, contentMetadata={'mid': receiver}, contentType=13)
                        elif cmd == 'getname':
                            me = client.getContact(to)
                            client.sendMessage(to,"「 DisplayName 」\n" + me.displayName)
                        elif cmd == 'getbio':
                            me = client.getContact(to)
                            client.sendMessage(to,"「 StatusMessage 」\n" + me.statusMessage)
                        elif cmd == 'getpic':
                            me = client.getContact(to)
                            client.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                        elif cmd == "getpicall":
                                kontak = client.getGroup(to)
                                group = kontak.members
                                for ids in group:
                                    client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/"+str(ids.pictureStatus))
                        elif cmd == 'getvid':
                            me = client.getContact(to)
                            client.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                        elif cmd == 'getcover':
                            if client != None:
                                path = client.getProfileCoverURL(to)
                                path = str(path)
                                if settings["server"] == "VPS":
                                    client.sendImageWithURL(to, str(path))
                                else:
                                    urllib.urlretrieve(path, "steal.jpg")
                                    client.sendImage(to, "steal.jpg")
                            else:
                                client.sendMessage(to, "Talk Exception")
                        elif cmd == 'getid':
                            if client != None:
                                me = client.getContact(to)
                                path = client.getProfileCoverURL(to)
                                path = str(path)
                                if settings["server"] == "VPS":
                                    client.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                                    client.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                                    client.sendMessage(msg.to,"「 MID 」\n" +  to)
                                    client.sendMessage(to, text=None, contentMetadata={'mid': to}, contentType=13)
                                    client.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                                    client.sendImageWithURL(to, str(path))
                                    client.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                else:
                                    client.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                                    client.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                                    client.sendMessage(msg.to,"「 MID 」\n" +  to)
                                    client.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                    client.sendImageWithURL(to, str(path))
                            else:
                                client.sendMessage(to, "Talk Exception")
#==============================================================================================================
                        elif cmd.startswith("getmid "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = ""
                                for ls in lists:
                                    ret_ += "{}".format(str(ls))
                                client.sendMessage(to, str(ret_))
                        elif cmd.startswith("getcontact "):
                            if client != None:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        me = client.getContact(ls)
                                    client.sendMessage(to, text=None, contentMetadata={'mid': ls}, contentType=13)
                        elif cmd.startswith("getname "):
                            if client != None:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        me = client.getContact(ls)
                                    client.sendMessage(msg.to,"「 DisplayName 」\n" + me.displayName)
                        elif cmd.startswith("getbio "):
                            if client != None:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        me = client.getContact(ls)
                                    client.sendMessage(msg.to,"「 StatusMessage 」\n" + me.statusMessage)
                        elif cmd.startswith("getpic "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.line.naver.jp/" + client.getContact(ls).pictureStatus
                                    if settings["server"] == "VPS":
                                        client.sendImageWithURL(to, str(path))
                                    else:
                                        urllib.urlretrieve(path, "steal.jpg")
                                        client.sendImage(to, "steal.jpg")
                        elif cmd.startswith("getcover "):
                            if client != None:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = client.getProfileCoverURL(ls)
                                        path = str(path)
                                        if settings["server"] == "VPS":
                                            client.sendImageWithURL(to, str(path))
                                        else:
                                            urllib.urlretrieve(path, "steal.jpg")
                                            client.sendImage(to, "steal.jpg")
                            else:
                                client.sendMessage(to, "Tidak dapat masuk di line channel")
                        elif cmd.startswith("getvid "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.line-cdn.net/" + client.getContact(ls).pictureStatus + "/vp"
                                    if settings["server"] == "VPS":
                                        client.sendVideoWithURL(to, str(path))
                                    else:
                                        client.sendMessage(to, "User doesnt have profile Video ^_^")
                        elif cmd.startswith("getid "):
                            if client != None:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        me = client.getContact(ls)
                                        path = client.getProfileCoverURL(ls)
                                        path = str(path)
                                        if settings["server"] == "VPS":
                                            client.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                                            client.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                                            client.sendMessage(msg.to,"「 MID 」\n" +  to)
                                            client.sendMessage(to, text=None, contentMetadata={'mid': ls}, contentType=13)
                                            client.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                                            client.sendImageWithURL(to, str(path))
                                            client.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                        else:
                                            client.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                                            client.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                                            client.sendMessage(msg.to,"「 MID 」\n" + ls)
                                            client.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                            client.sendImageWithURL(to, str(path))
                                    else:
                                        client.sendMessage(to, "Talk Exception You are not Related to LineChannel")
                            else:
                                 client.sendMessage(to, "Talk Exception You are not Related to LineChannel")
                        elif cmd == "getpicgroup":
                            if msg.toType == 2:
                                group = client.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                if settings["server"] == "VPS":
                                    client.sendImageWithURL(to, str(path))
                                else:
                                    urllib.urlretrieve(path, "gpict.jpg")
                                    client.sendImage(to, "gpict.jpg")
                        elif cmd.startswith("getpicgroup "):
                            saya = text.replace("getpicgroup ","")
                            gid = client.getGroupIdsJoined()
                            for i in gid:
                                h = client.getGroup(i).name
                                gna = client.getGroup(i)
                                if h == saya:
                                    path = ("http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
                                    client.sendImageWithURL(to,path)
                        elif cmd.startswith("getpic "):
                            saya = text.replace("getpic ","")
                            gid = client.getAllContactIds()
                            for i in gid:
                                h = client.getContact(i).displayName
                                gna = client.getContact(i)
                                if h == saya:
                                    path = ("http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
                                    client.sendImageWithURL(to,path)
#==============================================================================================================
                        elif cmd.startswith("clone "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    client.cloneContactProfile(contact)
                                    client.sendMessage(msg.to, "Operation Succes!")
                                except:
                                    client.sendMessage(msg.to, "Operation Failure!")
                        elif cmd.startswith("clonecover "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    client.CloneContactProfile(contact)
                                    client.sendMessage(msg.to, "Clone cover Succes!")
                                except:
                                    client.sendMessage(msg.to, "Operation Failure!")
                        elif cmd == 'restore':
                                try:
                                    clientProfile.displayName = str(myProfile["displayName"])
                                    clientProfile.statusMessage = str(myProfile["statusMessage"])
                                    clientProfile.pictureStatus = str(myProfile["pictureStatus"])
                                    client.updateProfileAttribute(8, clientProfile.pictureStatus)
                                    client.updateProfile(clientProfile)
                                    client.sendMessage(msg.to, "Restore profile succes!")
                                except:
                                    client.sendMessage(msg.to, "Gagal restore profile failure!")
#==============================================================================================================
                        elif cmd.startswith("spam "):
                            txt = text.split(" ")
                            jmlh = int(txt[2])
                            teks = text.replace("spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                            tulisan = jmlh * (teks+"\n")
                            if txt[1] == "on":
                                if jmlh <= 18000:
                                    for x in range(jmlh):
                                        client.sendMessage(to, teks)
                                else:
                                    client.sendMessage(to, "Out of range!")
                            elif txt[1] == "off":
                                if jmlh <= 18000:
                                    client.sendMessage(to, tulisan)
                                else:
                                    client.sendMessage(to, "Out of range!")
                        elif cmd.startswith("tag"):
                            sep = text.split(" ")
                            text = text.replace(sep[0] + " ","")
                            cond = text.split(" ")
                            jml = int(cond[0])
                            for x in range(jml):
                                name = client.getContact(to)
                                RhyN_(to, name.mid)
                        elif cmd == "stickers":
                            with open('sticker.json','r') as fp:
                                stickers = json.load(fp)
                            ret_ = "「Sticker List」"
                            for sticker in stickers:
                                ret_ += "\n    •" + sticker.title()
                            ret_ += "\n「Total {} Stickers」".format(str(len(stickers)))
                            client.sendMessage(to, ret_)
                        elif cmd == "listimage":
                            with open('anu.jpeg','r') as fp:
                                images = json.load(fp)
                            ret_ = "「Image List」"
                            for image in images:
                                ret_ += "\n    •" + image.title()
                            ret_ += "\n「Total {} Stickers」".format(str(len(images)))
                            client.sendMessage(to, ret_)
                        elif cmd.startswith("spamsticker "):
                            sep = text.split(" ")
                            text = text.replace(sep[0] + " ","")
                            cond = text.split(" ")
                            jml = int(cond[0])
                            stickername = str(cond[1]).lower()
                            with open('sticker.json','r') as fp:
                                stickers = json.load(fp)
                            if stickername in stickers:
                                sid = stickers[stickername]["STKID"]
                                spkg = stickers[stickername]["STKPKGID"]
                            else:
                                return
                            for x in range(jml):
                                client.sendSticker(to, spkg, sid)
#==============================================================================================================
                        elif cmd.startswith("gcast "):
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            groups = client.groups
                            for group in groups:
                                client.sendMessage(group, "「 Broadcasted 」\n{}".format(str(txt)))
                            client.sendMessage(to, "Succes Broadcasted to {} Groups".format(str(len(groups))))
                        elif cmd.startswith("pmcast "):
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            friends = client.friends
                            for friend in friends:
                                client.sendMessage(friend, "「 Broadcasted 」\n{}".format(str(txt)))
                            client.sendMessage(to, "Succes Broadcasted to {} Friends".format(str(len(friends))))
#==============================================================================================================
                        elif "/ti/g/" in msg.text.lower():
                            if settings["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = client.findGroupByTicket(ticket_id)
                                    client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    client.sendMessage(to, "Succes join to group %s" % str(group.name))
                        elif cmd.startswith("leave "):
                            ng = text.replace("leave ","")
                            gid = client.getGroupIdsJoined()
                            for i in gid:
                                h = client.getGroup(i).name
                                if h == ng:
                                    client.sendMessage(i,"Byebye "+h+"")
                                    client.leaveGroup(i)
                                    client.sendMessage(msg.to,"Success left ["+ h +"] group")
                                else:
                                    pass
#==============================================================================================================
                        elif cmd == "time" or cmd == "kalender":
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                            bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            anu = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nTime : 「 " + timeNow.strftime('%H:%M:%S') + " 」"
                            client.sendMessage(to, anu)
                        elif cmd == "speed" or cmd == "sp":
                            start = time.time()
                            client.sendMessage(to, "Progress..")
                            elapsed_time = time.time() - start
                            client.sendMessage(to, "{} Second".format(str(elapsed_time)))
                        elif cmd == "clearchat":
                            client.removeAllMessages(op.param2)
                            client.sendMessage(to, "Remove chat history")
                        elif cmd == "seeya":
                            if msg.toType == 2:
                                client.leaveGroup(to)
                        elif cmd == "gcreator":
                            ginfo = client.getGroup(to)
                            gCreator = ginfo.creator.mid
                            try:
                                gCreator1 = ginfo.creator.displayName
                            except:
                                gCreator = "Not Found"
                            client.sendMessage(to, text=None, contentMetadata={'mid': gCreator}, contentType=13)
                            sendMention(to, gCreator, "Hello", "Salken ya Kak Owner ^_^")
                        elif cmd == "ginfo":
                                    group = client.getGroup(to)
                                    gCreator = group.creator.mid
                                    try:
                                        gCreator1 = group.creator.displayName
                                    except:
                                        gCreator = "Not Found"
                                    if group.invitee is None:
                                        gPending = "0"
                                    else:
                                        gPending = str(len(group.invitee))
                                    if group.preventedJoinByTicket == True:
                                        gQr = "Refused"
                                        gTicket = "Nothing"
                                    else:
                                        gQr = "Open"
                                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                                    ret_ = "╔════════Grup Info═════════"
                                    ret_ += "\n╠Name Group : {}".format(group.name)
                                    ret_ += "\n╠ID Group : {}".format(group.id)
                                    ret_ += "\n╠Pic Group : http://dl.profile.line-cdn.net/" + str(group.pictureStatus)
                                    ret_ += "\n╠Group Creators  : {}".format(gCreator1)
                                    ret_ += "\n╠Group Members   : {}".format(str(len(group.members)))
                                    ret_ += "\n╠Pending Members : {}".format(gPending)
                                    ret_ += "\n╠Group QR        : {}".format(gQr)
                                    ret_ += "\n╠Group URL       : {}".format(gTicket)
                                    ret_ += "\n╚════════Grup Info═════════"
                                    client.sendMessage(to, str(ret_))
                                    client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/"+str(group.pictureStatus))
                                    client.sendMessage(to, text=None, contentMetadata={'mid': gCreator}, contentType=13)
                        elif cmd == "memberlist":
                                kontak = client.getGroup(to)
                                group = kontak.members
                                num=1
                                msgs="╔══[ Member List ]"
                                for ids in group:
                                    msgs+="\n╠[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n╚═════════════\n╔══════════════\n╠═[Total Members: %i]\n╚══════════════" % len(group)
                                client.sendMessage(to, msgs)
                        elif cmd == "grouplist":
                            groups = client.groups
                            ret_ = "╔══[ Group List ]"
                            no = 0
                            for gid in groups:
                                group = client.getGroup(gid)
                                ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                            client.sendMessage(to, str(ret_))
                        elif cmd == 'friendlist':
                            contactlist = client.getAllContactIds()
                            kontak = client.getContacts(contactlist)
                            num=1
                            msgs="╔════════[ Friend List ]"
                            for ids in kontak:
                                msgs+="\n╠[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n╚══════════════\n╔══════════════\n╠═[Total Friend: %i]\n╚══════════════" % len(kontak)
                            client.sendMessage(msg.to, msgs)
                        elif cmd == 'blocklist':
                            blockedlist = client.getBlockedContactIds()
                            kontak = client.getContacts(blockedlist)
                            num=1
                            msgs="╔════════[ Blocked List ]"
                            for ids in kontak:
                                msgs+="\n╠[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n╚══════════════\n╔══════════════\n╠═[Blocked Total: %i]\n╚══════════════" % len(kontak)
                            client.sendMessage(msg.to, msgs)
                        elif cmd == "blacklist" or cmd == "banlist":
                            if settings["blacklist"] == []:
                                client.sendMessage(to,"「Nothing」")
                            else:
                                num = 1
                                mc = "「BlackList」"
                                for me in settings["blacklist"]:
                                    mc += "\n\n    %i•  %s" % (num, client.getContact(me).displayName)
                                    num = (num+1)
                                mc += "\n\n「Total %i BlackList」" % len(settings["blacklist"])
                                client.sendMessage(to, mc)
                        elif cmd.startswith("gn "):
                            sep = text.split(" ")
                            if msg.toType == 2:
                                try:
                                    group = client.getGroup(to)
                                    group.name = text.replace(sep[0] + " ","")
                                    client.updateGroup(group)
                                except:
                                    pass
                        elif cmd == "url" or cmd == "ourl":
                            if msg.toType == 2:
                                g = client.getGroup(msg.to)
                                if g.preventedJoinByTicket == True:
                                    g.preventedJoinByTicket = False
                                    client.updateGroup(g)
                                gurl = client.reissueGroupTicket(msg.to)
                                client.sendMessage(msg.to,"「Group Link」\n\n\nhttp://line.me/R/ti/g/" + gurl)
                        elif cmd == "curl" or cmd == "close":
                            if msg.toType == 2:
                                group = client.getGroup(msg.to)
                                group.preventedJoinByTicket = True
                                client.updateGroup(group)
#==============================================================================================================
                        elif cmd == "lurking on":
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nTime : 「 " + timeNow.strftime('%H:%M:%S') + " 」"
                                if msg.to in read['readPoint']:
                                        try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                        except:
                                            pass
                                        read['readPoint'][msg.to] = msg.id
                                        read['readMember'][msg.to] = ""
                                        read['readTime'][msg.to] = datetime.datetime.now().strftime('%H:%M:%S')
                                        read['ROM'][msg.to] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(read, fp, sort_keys=True, indent=4)
                                            client.sendMessage(msg.to,"Lurking already on")
                                else:
                                    try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][msg.to] = msg.id
                                    read['readMember'][msg.to] = ""
                                    read['readTime'][msg.to] = datetime.datetime.now().strftime('%H:%M:%S')
                                    read['ROM'][msg.to] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(read, fp, sort_keys=True, indent=4)
                                        client.sendMessage(msg.to, "Set reading point:\n" + readTime)
                        elif cmd == "lurking off":
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nTime : 「 " + timeNow.strftime('%H:%M:%S') + " 」"
                                if msg.to not in read['readPoint']:
                                    client.sendMessage(msg.to,"Lurking already off")
                                else:
                                    try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                    except:
                                          pass
                                    client.sendMessage(msg.to, "Delete reading point:\n" + readTime)
                        elif cmd == 'lurking reset':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.datetime.now()
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nTime : 「 " + timeNow.strftime('%H:%M:%S') + " 」"
                                if msg.to in read["readPoint"]:
                                    try:
                                        read["readPoint"][msg.to] = True
                                        read["readMember"][msg.to] = {}
                                        read["readTime"][msg.to] = readTime
                                        read["ROM"][msg.to] = {}
                                    except:
                                        pass
                                    client.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                                else:
                                    client.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        elif cmd == 'lurking result':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.datetime.now()
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
                                bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nTime : 「 " + timeNow.strftime('%H:%M:%S') + " 」"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        client.sendMessage(receiver,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = client.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '「 Lurkers 」\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n" + readTime
                                    try:
                                        client.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    client.sendMessage(receiver,"Lurking has not been set.")
#==============================================================================================================
                        elif cmd == "sider:on" or cmd == "cek sider:on":
                            try:
                                del cctv['point'][receiver]
                                del cctv['sidermem'][receiver]
                                del cctv['cyduk'][receiver]
                            except:
                                pass
                            cctv['point'][receiver] = msg.id
                            cctv['sidermem'][receiver] = ""
                            cctv['cyduk'][receiver]=True
                            client.sendMessage(receiver, "Auto checking sider set to on")
                        elif cmd == "sider:off" or cmd == "cek sider:off":
                            if msg.to in cctv['point']:
                                cctv['cyduk'][receiver]=False
                                client.sendMessage(receiver, cctv['sidermem'][msg.to])
                            else:
                                client.sendMessage(receiver, "Auto checking sider set to off")
#==============================================================================================================
                        elif cmd == "set":
                            md = "Settings Bots♪ \n\n"
                            if settings["autoRead"] == True: md+="「✦」  • Autoread♪\n"
                            else: md+="「✧」  • Autoread♪\n"
                            if settings["mimic"]["status"] == True: md+="「✦」  • Mimic♪\n"
                            else: md+="「✧」  • Mimic♪\n"
                            if settings["autoAdd"] == True: md+="「✦」  • Autoadd♪\n"
                            else: md+="「✧」  • Autoadd♪\n"
                            if settings["autoLeave"] == True: md+="「✦」  • AutoLeave♪\n"
                            else: md+="「✧」  • AutoLeave♪\n"
                            if settings["autoJoin"] == True: md+="「✦」  • Autojoin♪\n"
                            else: md+="「✧」  • Autojoin♪\n"
                            if settings["autoJoinTicket"] == True: md+="「✦」  • AutojoinQr♪\n"
                            else: md+="「✧」  • AutojoinQr♪\n"
                            if settings["checkContact"] == True: md+="「✦」  • DisplayContact♪\n"
                            else: md+="「✧」  • DisplayContact♪\n"
                            if settings["protect"] == True: md+="「✦」  • Protection\n"
                            else: md+="「✧」  • Protection\n"
                            if settings["pinvite"] == True: md+="「✦」  • ProtectInvite\n"
                            else: md+="「✧」  • ProtectInvite\n"
                            if settings["qrp"] == True: md+="「✦」  • ProtectURL\n"
                            else: md+="「✧」  • ProtectURL\n"
                            if settings["pcancel"] == True: md+="「✦」  • StrictMode\n"
                            else: md+="「✧」  • StrictMode\n"
                            client.sendMessage(to,md)
#====================
                        elif cmd == "autoadd on":
                            settings["autoAdd"] = True
                            client.sendMessage(to, "Autoadd set to on♪")
                        elif cmd == "autoadd off":
                            settings["autoAdd"] = False
                            client.sendMessage(to, "Autoadd set to off♪")
#====================
                        elif cmd == "qrjoin on":
                            settings["autoJoinTicket"] = True
                            client.sendMessage(to, "Autojointicket set to on♪")
                        elif cmd == "qrjoin off":
                            settings["autoJoinTicket"] = False
                            client.sendMessage(to, "Autojointicket set to off♪")
#====================
                        elif cmd == "dc on" or cmd == "k on":
                            settings["checkContact"] = True
                            client.sendMessage(to, "Display contact set to on♪")
                        elif cmd == "dc off" or cmd == "k off":
                            settings["checkContact"] = False
                            client.sendMessage(to, "Display contact set to off♪")
#====================
                        elif cmd == "autojoin on":
                            settings["autoJoin"] = True
                            client.sendMessage(to, "Autojoin set to on♪")
                        elif cmd == "autojoin off":
                            settings["autoJoin"] = False
                            client.sendMessage(to, "Autojoin set to off♪")
#====================
                        elif cmd == "autoleave on":
                            settings["autoLeave"] = True
                            client.sendMessage(to, "AutoLeave set to on♪")
                        elif cmd == "autoleave off":
                            settings["autoLeave"] = False
                            client.sendMessage(to, "AutoLeave set to off♪")
#====================
                        elif cmd == "autoread on":
                            settings["autoRead"] = True
                            client.sendMessage(to, "AutoRead set to on♪")
                        elif cmd == "autoread off":
                            settings["autoRead"] = False
                            client.sendMessage(to, "AutoRead set to off♪")
#====================
                        elif cmd == "protect on":
                            settings["protect"] = True
                            client.sendMessage(to, "Protection set to on♪")
                        elif cmd == "protect off":
                            settings["protect"] = False
                            client.sendMessage(to, "Protection set to off♪")
#====================
                        elif cmd == "invite on":
                            settings["pinvite"] = True
                            client.sendMessage(to, "Protect invitation set to on♪")
                        elif cmd == "invite off":
                            settings["pinvite"] = False
                            client.sendMessage(to, "Protect invitation set to off♪")
#====================
                        elif cmd == "cancel on":
                            settings["pcancel"] = True
                            client.sendMessage(to, "Protection cancel set to on♪")
                        elif cmd == "cancel off":
                            settings["pcancel"] = False
                            client.sendMessage(to, "Protection cancel set to off♪")
#====================
                        elif cmd == "qr on":
                            settings["qrp"] = True
                            client.sendMessage(to, "Protection Qr set to on♪")
                        elif cmd == "qr off":
                            settings["qrp"] = False
                            client.sendMessage(to, "Protection Qr set to off♪")
#==============================================================================================================
                        elif "mimic " in msg.text.lower():
                            mic = msg.text.lower().replace("mimic ","")
                            if mic == "on":
                                if settings["mimic"]["status"] == False:
                                    settings["mimic"]["status"] = True
                                    client.sendMessage(msg.to,"Mimic set to on♪")
                                else:
                                    client.sendMessage(msg.to,"Mimic already on♪")
                            elif mic == "off":
                                if settings["mimic"]["status"] == True:
                                    settings["mimic"]["status"] = False
                                    client.sendMessage(msg.to,"Mimic set to off♪")
                                else:
                                    client.sendMessage(msg.to,"Mimic already off♪")
#==============================================================================#
                        elif msg.text.lower().startswith("mimicadd "):
                            targets = []
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                try:
                                    settings["mimic"]["target"][target] = True
                                    client.sendMessage(msg.to,"Target ditambahkan!")
                                    break
                                except:
                                    client.sendMessage(msg.to,"Added Target Fail !")
                                    break
                        elif msg.text.lower().startswith("mimicdel "):
                            targets = []
                            key = eval(msg.contentMetadata["MENTION"])
                            key["MENTIONEES"][0]["M"]
                            for x in key["MENTIONEES"]:
                                targets.append(x["M"])
                            for target in targets:
                                try:
                                    del settings["mimic"]["target"][target]
                                    client.sendMessage(msg.to,"Target dihapuskan!")
                                    break
                                except:
                                    client.sendMessage(msg.to,"Deleted Target Fail !")
                                    break
                        elif text.lower() == 'mimiclist':
                            if settings["mimic"]["target"] == {}:
                                client.sendMessage(msg.to,"Target in Mimic List None♪")
                            else:
                                num = 1
                                mc = "╔══「 MimicList 」"
                                for mi_d in settings["mimic"]["target"]:
                                    mc += "\n╠ • "+client.getContact(mi_d).displayName
                                mc += "\n╚══「 Finish 」"
                                client.sendMessage(msg.to,mc)
#==============================================================================================================
                        elif cmd.startswith("ss "):
                            query = text.replace("ss ","")
                            with requests.session() as web:
                                r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                data = r.text
                                data = json.loads(data)
                                client.sendImageWithURL(to, data["result"])
                        elif cmd.startswith("checkdate "):
                            tanggal = text.replace("checkdate ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            ret_ = "╔══[ D A T E ]"
                            ret_ += "\n╠ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                            ret_ += "\n╠ Age : {}".format(str(data["data"]["usia"]))
                            ret_ += "\n╠ Birthday : {}".format(str(data["data"]["ultah"]))
                            ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                            ret_ += "\n╚══[ Success ]"
                            client.sendMessage(to, str(ret_))
                        elif cmd.startswith("igpost "):
                            user = text.replace("igpost ","")
                            profile = "https://www.instagram.com/" + user
                            with requests.session() as x:
                                x.headers['user-agent'] = 'Mozilla/5.0'
                                end_cursor = ''
                                for count in range(1, 999):
                                    print('PAGE: ', count)
                                    r = x.get(profile, params={'max_id': end_cursor})
                                    data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                                    j = json.loads(data)
                                    for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                        if node['is_video']:
                                            page = 'https://www.instagram.com/p/' + node['code']
                                            r = x.get(page)
                                            url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                            print(url)
                                            client.sendVideoWithURL(msg.to,url)
                                        else:
                                            print (node['display_src'])
                                            client.sendImageWithURL(msg.to,node['display_src'])
                                    end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)
                        elif cmd.startswith("getimage "):
                            search = text.replace("getimage ","")
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    items = data["result"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    client.sendImageWithURL(to, str(path))
                                else:
                                    client.sendMessage(to, str(data["error"]))
                        elif cmd.startswith("ig "):
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                params = {'igid': instagram}
                                with requests.session() as web:
                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                    r = web.get("https://www.instagram.com/"+instagram+"?__a=1")
                                    try:
                                        data = r.json()
                                        namaIG = str(data['user']['full_name'])
                                        bioIG = str(data['user']['biography'])
                                        mediaIG = str(data['user']['media']['count'])
                                        verifIG = str(data['user']['is_verified'])
                                        usernameIG = str(data['user']['username'])
                                        followerIG = str(data['user']['followed_by']['count'])
                                        profileIG = data['user']['profile_pic_url_hd']
                                        privateIG = str(data['user']['is_private'])
                                        followIG = str(data['user']['follows']['count'])
                                        link = "Link: " + "https://www.instagram.com/" + instagram + ""
                                        detail = "╔═══════════[ INSTAGRAM INFO ]\n"
                                        details = "\n╚═══════════════════[ Finish ]"
                                        text = detail + "╠ Name : "+namaIG+"\n╠ Username : "+usernameIG+"\n╠ Biography : "+bioIG+"\n╠ Follower : "+followerIG+"\n╠ Following : "+followIG+"\n╠ Post : "+mediaIG+"\n╠ Verified : "+verifIG+"\n╠ Private : "+privateIG+"" "\n╠ " + link + details
                                        client.sendMessage(to, str(text))
                                        client.sendImageWithURL(to, profileIG)
                                    except Exception as e:
                                        client.sendMessage(to, str(e))
                        elif cmd.startswith("wikipedia "):
                                try:
                                    sep = msg.text.split(" ")
                                    wiki = msg.text.replace(sep[0] + " ","")
                                    wikipedia.set_lang("id")
                                    pesan="╔═══「Title : "
                                    pesan+=wikipedia.page(wiki).title
                                    pesan+=" 」\n╠「Isi : "
                                    pesan+=wikipedia.summary(wiki, sentences=1)
                                    pesan+=" 」\n╠「Link : "+wikipedia.page(wiki).url
                                    pesan+=" 」\n╚═════════════[ Finish ]"
                                    client.sendMessage(to, pesan)
                                except:
                                        try:
                                            pesan="Over Text Limit! Please Click link\n"
                                            pesan+=wikipedia.page(wiki).url
                                            client.sendMessage(to, pesan)
                                        except Exception as e:
                                            client.sendMessage(to, str(e))
                        elif cmd.startswith("checkpraytime "):
                            sep = text.split(" ")
                            location = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashr : " and data[4] != "Maghrib : " and data[5] != "Isya' : ":
                                    ret_ = "「 PRAYER SCHEDULE 」"
                                    ret_ += "\n   • Location: " + data[0]
                                    ret_ += "\n   • " + data[1]
                                    ret_ += "\n   • " + data[2]
                                    ret_ += "\n   • " + data[3]
                                    ret_ += "\n   • " + data[4]
                                    ret_ += "\n   • " + data[5]
                                    ret_ += "\n「 Done 」"
                                else:
                                    ret_ = "[ Prayer Schedule ] Error : Location Not found!" 
                                client.sendMessage(to, str(ret_))
                        elif cmd.startswith("checkweather "):
                            sep = text.split(" ")
                            location = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if "result" not in data:
                                    ret_ = "「 WHEATER STATUS 」"
                                    ret_ += "\n   • Location: " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n   • Temperature: " + data[1].replace("Suhu : ","")
                                    ret_ += "\n   • Humidity: " + data[2].replace("Kelembaban : ","")
                                    ret_ += "\n   • Air pressure: " + data[3].replace("Tekanan udara : ","")
                                    ret_ += "\n   • Wind Velocity: " + data[4].replace("Kecepatan angin : ","")
                                    ret_ += "\n「 Weather Status Complete 」"
                                else:
                                    ret_ = "[ Weather Status ] Error : Location Not found!"
                                client.sendMessage(to, str(ret_))
                        elif cmd.startswith("checklocation "):
                            sep = text.split(" ")
                            location = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「 DETAILS LOCATION 」"
                                    ret_ += "\n   • Location: " + data[0]
                                    ret_ += "\n   • Google Maps: " + link
                                    ret_ += "\n「 Location Status Complete 」"
                                else:
                                    ret_ = "[ Details Location ] Error : Location Not found!"
                                client.sendMessage(to,str(ret_))
                        elif cmd.startswith("getmusic "):
                                sep = msg.text.split(" ")
                                textnya = msg.text.replace(sep[0] + " ","")
                                params = {'songname': textnya}
                                with requests.session() as web:
                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                    r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
                                    try:
                                        data = json.loads(r.text)
                                        for song in data:
                                            ret_ = "「 Music 」"
                                            ret_ += "\n   • Nama lagu : {}".format(str(song[0]))
                                            ret_ += "\n   • Durasi : {}".format(str(song[1]))
                                            ret_ += "\n   • Link : {}".format(str(song[3]))
                                            ret_ += "\n「 Finish 」"
                                            client.sendMessage(msg.to, str(ret_))
                                            client.sendMessage(msg.to, "Please wait for audio")
                                            client.sendAudioWithURL(msg.to, song[3])
                                    except:
                                        client.sendMessage(msg.to, "Musik tidak ditemukan")
                        elif cmd.startswith("music "):
                                sep = msg.text.split(" ")
                                textnya = msg.text.replace(sep[0] + " ","")
                                params = {'songname': textnya}
                                with requests.session() as web:
                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                    r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
                                    try:
                                        data = json.loads(r.text)
                                        for song in data:
                                            songs = song[5]
                                            lyric = songs.replace('ti:','Title - ')
                                            lyric = lyric.replace('ar:','Artist - ')
                                            lyric = lyric.replace('al:','Album - ')
                                            removeString = "[1234567890.:]"
                                            for char in removeString:
                                                lyric = lyric.replace(char,'')
                                            ret_ = "「 Music And Lyrics 」"
                                            ret_ += "\n   • Nama lagu : {}".format(str(song[0]))
                                            ret_ += "\n   • Durasi : {}".format(str(song[1]))
                                            ret_ += "\n   • Link : {}".format(str(song[3]))
                                            ret_ += "\n「 Finish 」\n{}".format(str(lyric))
                                            client.sendMessage(msg.to, str(ret_))
                                            client.sendMessage(msg.to, "Please wait for audio")
                                            client.sendAudioWithURL(msg.to, song[3])
                                    except:
                                        client.sendMessage(msg.to, "Musicnya not found!")
                        elif cmd.startswith("imagetext "):
                                sep = msg.text.split(" ")
                                textnya = msg.text.replace(sep[0] + " ","")
                                path = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                                client.sendImageWithURL(msg.to,path)
                        elif cmd.startswith("getvideo "):
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                dl=("https://www.youtube.com" + results['href'])
                                vid = pafy.new(dl)
                                stream = vid.streams
                                for s in stream:
                                    vin = s.url
                                    hasil = "「 Video 」"
                                    hasil += "\n╠ Title : {}".format(str(vid.title))
                                    hasil += "\n╠ Subscriber From : {}".format(str(vid.author))
                                    hasil += "\n╠ Please wait for the videos"
                                    hasil += "\n╚═══════════════════[ Finish ]"
                                client.sendMessage(msg.to,hasil)
                                client.sendVideoWithURL(msg.to,vin)
                                print("[YOUTUBE]MP4 Succes")
                            except Exception as e:
                                client.sendMessage(to, str(e))
#==============================================================================================================
                        elif cmd.startswith("ban:on "):
                            sep = text.split(" ")
                            text = text.replace(sep[0] + " ","")
                            if msg.toType == 2:
                                group = client.getGroup(to)
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for target in lists:
                                            try:
                                                settings["blacklist"][target] = True
                                                del settings["whitelist"][target]
                                                f=codecs.open('st2__b.json','w','utf-8')
                                                json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                                client.sendMessage(to,"")
                                                print("[Command] Bannad")
                                            except:
                                                pass
                        elif cmd.startswith("unban:on "):
                            sep = text.split(" ")
                            text = text.replace(sep[0] + " ","")
                            if msg.toType == 2:
                                group = client.getGroup(to)
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for target in lists:
                                            try:
                                                del settings["blacklist"][target]
                                                f=codecs.open('st2__b.json','w','utf-8')
                                                json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                                client.sendMessage(to,"")
                                                print("[Command] Bannad")
                                            except:
                                                pass
                        elif cmd == "ban:on":
                            settings["wblacklist"] = True
                            client.sendMessage(to,"Send Contact to Ban")
                        elif cmd == "unban:on":
                            settings["dblacklist"] = True
                            client.sendMessage(to,"Send Contact to Unban")
                        elif cmd == "blc" or cmd == "mute contact":
                            if msg._from in clientMID:
                                if settings["blacklist"] == []:
                                    client.sendMessage(to, "Nothing boss")
                                else:
                                    for bl in settings["blacklist"]:
                                        client.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                        elif cmd == "clearban":
                            settings["blacklist"] = {}
                            client.sendMessage(to,"「Blacklist clear」")
                        elif cmd == "bl contact":
                            if msg._from in clientMID:
                                blockedlist = client.getBlockedContactIds()
                                if blockedlist == []:
                                    client.sendMessage(to, "Gada yg di BLOCK!")
                                else:
                                    for kontak in blockedlist:
                                        client.sendMessage(to, text=None, contentMetadata={'mid': kontak}, contentType=13)
#==============================================================================================================
                        elif cmd == "mention" or cmd == "tagall" or cmd == "desah" or cmd == "jembot":
                            group = client.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//100
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*100 : (a+1)*100]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@RhyN_\n'
                                client.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
#==============================================================================================================
#=====================================================[]=======================================================
#==============================================================================================================
                if msg.contentType == 13:
                    if settings["wblacklist"] == True:
                        if msg.contentMetadata["mid"] in settings["blacklist"]:
                            client.sendMessage(to,"「Done」")
                            settings["wblacklist"] = False
                        else:
                            settings["blacklist"][msg.contentMetadata["mid"]] = True
                            settings["wblacklist"] = False
                            client.sendMessage(to,"「Done」")
                    elif settings["dblacklist"] == True:
                        if msg.contentMetadata["mid"] in settings["blacklist"]:
                            del settings["blacklist"][msg.contentMetadata["mid"]]
                            client.sendMessage(to,"「Done」")
                            settings["dblacklist"] = False
                        else:
                            settings["dblacklist"] = False
                            client.sendMessage(to,"「Done」")
#==============================================================================================================
#=====================================================[]=======================================================
#==============================================================================================================
                if msg.contentType == 13:
                    if settings["checkContact"] == True:
                        msg.contentType = 0
                        client.sendMessage(msg.to,msg.contentMetadata["mid"])
                        if 'displayName' in msg.contentMetadata:
                            contact = client.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = client.getProfileCoverURL(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            client.sendMessage(msg.to,"「DisplayName」:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                        else:
                            contact = client.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = client.getProfileCoverURL(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            if settings["server"] == "VPS":
                                client.sendMessage(msg.to, "「DisplayName」:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                                client.sendImageWithURL(msg.to, "http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                                client.sendImageWithURL(msg.to, str(cu))
#==============================================================================================================
#=====================================================[]=======================================================
#==============================================================================================================
                if msg.contentType == 1:
                    if settings["changePicture"] == True:
                        path = client.downloadObjectMsg(msg_id)
                        settings["changePicture"] = False
                        client.updateProfilePicture(path)
                        client.sendMessage(to, "Change profile picture Succes")
                    if msg.toType == 2:
                        if to in settings["changeGroupPicture"]:
                            path = client.downloadObjectMsg(msg_id)
                            settings["changeGroupPicture"].remove(to)
                            client.updateGroupPicture(to, path)
                            client.sendMessage(to, "Change group picture Succes")
#==============================================================================================================
#=====================================================[]=======================================================
#==============================================================================================================
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != client.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#========================================================================                    
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                        contact = client.getContact(sender)
                        txt = '[%s] %s' % (contact.displayName, text)
                        client.log(txt)
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    if msg.contentType == 7:
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        ret_ = "╔══[ Sticker Info ]"
                        ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                        ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                        ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                        client.sendMessage(to, text=None, contentMetadata={'STKID':'107', 'STKVER':'100', 'STKPKGID':'1'}, contentType=7)
                    elif msg.contentType == 1:
                        client.sendMessage(to, text=None, contentMetadata={"STKID": "190", "STKVER": "100", "STKPKGID": "3"}, contentType=7)
                    else:
                        if text is not None:
                            txt = text
                            client.sendMessage(msg.to,txt)
                    
#==============================================================================================================
#=====================================================[]=======================================================
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = assist1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        assist1.updateGroup(G)
                        Ticket = assist1.reissueGroupTicket(op.param1)
                        client.acceptGroupInvitationByTicket(op.param1,Ticket)
                        assist2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        assist1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventedJoinByTicket = True
                        client.updateGroup(G)
                    else:
                        G = assist1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        assist1.updateGroup(G)
                        Ticket = assist1.reissueGroupTicket(op.param1)
                        client.acceptGroupInvitationByTicket(op.param1,Ticket)
                        assist2.kickoutFromGroup(op.param1,[op.param2])
                        assist2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        assist1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventedJoinByTicket = True
                        client.updateGroup(G)
                        assist2.updateGroup(G)
                        assist1.updateGroup(G)
                        assist2.updateGroup(G)
                if op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = assist2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        assist2.updateGroup(G)
                        Ticket = assist2.reissueGroupTicket(op.param1)
                        assist1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        client.acceptGroupInvitationByTicket(op.param1,Ticket)
                        assist2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventedJoinByTicket = True
                        assist2.updateGroup(G)
                    else:
                        G = assist2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        assist2.updateGroup(G)
                        Ticket = assist2.reissueGroupTicket(op.param1)
                        assist1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        assist2.kickoutFromGroup(op.param1,[op.param2])
                        assist2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        client.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventedJoinByTicket = True
                        assist1.updateGroup(G)
                        assist2.updateGroup(G)
                        client.updateGroup(G)
                        assist1.updateGroup(G)
                        assist2.updateGroup(G)
                if op.param3 in ki2mid:
                    if op.param2 in mid:
                        G = client.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        client.updateGroup(G)
                        Ticket = client.reissueGroupTicket(op.param1)
                        assist2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventedJoinByTicket = True
                        client.updateGroup(G)
                        assist2.updateGroup(G)
                        assist1.updateGroup(G)
                    else:
                        G = client.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        client.updateGroup(G)
                        Ticket = client.reissueGroupTicket(op.param1)
                        assist2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        assist1.kickoutFromGroup(op.param1,[op.param2])
                        assist1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        client.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventedJoinByTicket = True
                        assist1.updateGroup(G)
                        assist2.updateGroup(G)
                        assist1.updateGroup(G)
                        client.updateGroup(G)
            except:
                pass
#==============================================================================================================
        if op.type == 32:
            if settings["pcancel"] == True:
                if op.param2 in Bots:
                    pass
                else:
                    try:
                        group = client.getGroup(op.param1)
                        group.preventedJoinByTicket = True
                        Ticket = assist.reissueGroupTicket(op.param1)
                        assist3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        assist3.kickoutFromGroup(op.param1,[op.param2])
                        assist3.sendMessage(op.param1, text=None, contentMetadata={'mid': op.param2}, contentType=13)
                        group = assist2.getGroup(op.param1)
                        group.preventedJoinByTicket = True
                        assist2.updateGroup(group)
                        assist3.leaveGroup(op.param1)
                        settings["blacklist"][op.param2] = True
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    except:
                        pass
#==============================================================================================================
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                zxn=["Jangan sider terus ","Jangan sider ","Halo ayo kita ngobrol ","Turun kak ikut chat ","Sider mulu ","sider tak doakan jones ","Ciyyee yang lagi ngintip ","Hai Kang ngintip ","Jangan sider mulu dong kk ","Bintitan kapok lu"]
                                client.sendMessage(op.param1, str(random.choice(zxn))+' '+Name)                                                              
                                dhil(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
        else:
            pass
#==============================================================================================================
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================================================
def cium(to, nama):
    aa = ""
    bb = ""
    strt = int(0)
    akh = int(0)
    nm = nama
    myid = "u2e530aebeb333246a68c347abff44b4cn"
    if myid in nm:    
      nm.remove(myid)
    #print nm
    for mm in nm:
      akh = akh + 6
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 7
      akh = akh + 1
      bb += "@FUCK \n"
    aa = (aa[:int(len(aa)-1)])
    text = bb
    try:
       client.sendMessage(to, text, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
       print(error)
#==============================================================================================================
#==============================================================================================================
def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in settings['readPoint']:
                    if msg._from in settings["ROM"][msg.to]:
                        del settings["ROM"][msg.to][msg._from]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as error:
        print(error)
        print("\n\nRECEIVE_MESSAGE\n\n")
        return
#==============================================================================================================
def atend():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    time.sleep(10)
    python = sys.executable
    os.execl(python, python, *sys.argv)
#==============================================================================================================
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#==============================================================================================================
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)