from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from mp.models import Mentor

# Create your views here.
def index(request):
	all_mentors = Mentor.objects.all()
	home = []
	major = []
	year = ['大二', '大三', '大四']
	for mentor in all_mentors:
		if mentor.home not in home:
			home.append(mentor.home)
		if mentor.major not in major:
			major.append(mentor.major)
	return render_to_response('mp/indexView.html',{'home':home, 'major':major,'year':year})

def all(request):
	all_mentors = Mentor.objects.all()
	return render_to_response('mp/allView.html',{'all_mentors':all_mentors})

def mentor(request, mentor_id):
	mentor = Mentor.objects.get(pk=mentor_id)
	key = ["Email","性别", "年级", "学院", "家乡", "高中", "专业", "以后工作方向","自我介绍","课外活动", "兴趣爱好","用三个词形容你的性格", "推荐的几门UVA的课", "最喜欢的音乐 歌曲 歌手", "最喜欢的电影 动漫 电视剧", "最喜欢的文学 作品 书籍", "最喜欢的一句quote"]
	email = mentor.email
	gender = mentor.gender
	year = mentor.year
	school = mentor.school
	home = mentor.home
	high = mentor.high
	major = mentor.major
	work = mentor.work
	intro = mentor.intro
	ec = mentor.ec
	hobby = mentor.hobby
	three = mentor.three
	clas = mentor.clas
	music = mentor.music
	movie = mentor.movie
	book = mentor.book
	quote = mentor.quote
	value = [email, gender, year, school, home, high, major, work, intro, ec, hobby,three, clas, music, movie, book, quote]
	h = zip(key,value)
	return render_to_response('mp/mentorView.html',{'mentor':mentor, 'h':h})

def home(request):
	home = request.GET
	all_mentors = []
	for h in home:
		temp = Mentor.objects.filter(home=h)
		all_mentors.extend(temp)
	return render_to_response('mp/homeView.html',{'home':home,'all_mentors':all_mentors})

def major(request):
	major = request.GET
	all_mentors = []
	for m in major:
		temp = Mentor.objects.filter(major=m)
		all_mentors.extend(temp)
	return render_to_response('mp/majorView.html',{'major':major,'all_mentors':all_mentors})

def year(request):
	year = request.GET
	all_mentors = []
	for y in year:
		temp = Mentor.objects.filter(year=y)
		all_mentors.extend(temp)
	return render_to_response('mp/yearView.html',{'year':year,'all_mentors':all_mentors})