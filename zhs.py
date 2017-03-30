# -*-coding:utf-8 -*-

import requests
import browser
import pyquery
import json

validateParams = {
	'account': 18728193496,
	'password': 520999
}

browser = browser.Browser()

# validate & login
validateR = browser.session.post(
	'http://passport.zhihuishu.com/user/validateAccountAndPassword',
	params = validateParams
)

print validateR.text

# request login page
loginFormR = browser.session.get('http://passport.zhihuishu.com/login?service=http://online.zhihuishu.com/onlineSchool/')

# print loginFormR.text

lt = pyquery.PyQuery(loginFormR.text)('input[name=lt]').val()
execution = pyquery.PyQuery(loginFormR.text)('input[name=execution]').val()

loginParams = {
	'username': 18728193496,
	'password': 520999,
	'execution': execution,
	'_eventId': 'submit',
	'lt': lt
}

loginR = browser.session.post(
	'https://passport.zhihuishu.com/login',
	allow_redirects=True,
	data = loginParams
)

print loginR.status_code

# print loginR.text

# get list (dataType=0)
listParams = {
	'dataType': 0 # dataType=1 已完成的
}

requests.get('http://online.zhihuishu.com/onlineSchool/student/index')

listR = browser.session.post('http://online.zhihuishu.com/onlineSchool/json/student/loadStuCourseRecruit', params = listParams)

listObject = listR.text

# print listObject

# 完成某个章节
coursePageUrl = 'http://online.zhihuishu.com/CreateCourse/learning/videoList?courseId=2009195&rid=4066';

coursePageR = browser.session.get(coursePageUrl)

pyquery.PyQuery(coursePageR)('#video-103188');

# 刷课
# courseParams = {
#     '__learning_token__':'MjI4Mjc2ODYy',
#     'studiedLessonDto.learnTime':'00:17:11',
#     'studiedLessonDto.studyTotalTime':1400,
#     'studiedLessonDto.playTimes':80,
#     'studiedLessonDto.recruit.id':4066,
#     'studiedLessonDto.lessonVideo.id': 94467,
#     'studiedLessonDto.lesson.id':101143,
#     'studiedLessonDto.videoId':103193,
#     'studyStatus': '',
#     'csrfToken':'onlkXtqSaMW6KGCb'
# }

# a = browser.session.post(
#     'http://online.zhihuishu.com/CreateCourse/json/learning/saveDatabaseIntervalTime?time=1490535732561',
#     data = courseParams
# )

# print a.text

# 答案保存在缓存中
cacheUrl = 'http://exam.zhihuishu.com/onlineExam/studentHomework/cacheAnswerDto.action'

cacheParmas = {
	"studentExam.id": 98978581,
	"studentExam.userId": 161109715,
	"studentExam.exam.id": 46642,
	"studentExam.recruit.id": 4066
}

# cookie = {
# 	"answerDtos": [
# 		{
# 			"answerDto.testQuestion.id": "225152",
# 			"answerDto.answer": "839160",
# 			"answerDto.stuExamId": "98978581"
# 		}
# 	]
# }

arr = [
	{
		"answerDto.testQuestion.id": "225152",
		"answerDto.answer": "839160",
		"answerDto.stuExamId": "98978581"
	}
]

# cookie = '{ "a": 123 }'
jar = requests.cookies.RequestsCookieJar()

jar.set('answerDtos', arr)

test = browser.session.post(
	cacheUrl,
	data = cacheParmas
)

print test


# 提交考试
examUrl = 'http://exam.zhihuishu.com/onlineExam/studentHomework/saveAnswer.action'

examParams = {
	"studentExam.id": 98978581,
    "studentExam.achieveCount": 1,
    "studentExam.state": 1,
    "studentExam.examId": 46642,
    "studentExam.recruitId": 4066,
    "studentExam.courseId": 2009195,
    "studentExam.lateState": 0,
    "questionIds": [225152]
}

examR = browser.session.post(
	examUrl,
	data = examParams
)

