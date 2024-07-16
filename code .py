import telebot

API_KEY= ("your telegram api key")

bot= telebot.TeleBot(API_KEY) #api key 

@bot.message_handler(commands=['start','hello'])
def start(message):
t.send_message(message.chat.id,"for btech type /btech")
@bot.message_handler(commands=['btech'])
#def btech(message):
    #bot.send_message(message.chat.id,"chose the course")
 #   bot.send_message(message.chat.id,"for computer sience type /cs")
    #bot.send_message(message.chat.id,"for civil type /civ")
    #bot.send_message(message.chat.id,"for biotech type /bt")
    #bot.send_message(message.chat.id,"for mechinal type /mec")
@bot.message_handler(commands=['btech'])
#@bot.InlineKeyboardButton('btech','button1')
def cs(message):
       # bot.menu_button(commands=['btech'])
        #bot.send_message(message.chat.id,"Bhai kya")
        #pic='https://humornama.com/wp-content/uploads/2022/02/Bhai-Kya-Kar-Raha-Hai-Tu-Meme-Template-on-Ashneer-Grover-1024x614.jpg'
        #bot.send_photo(message.chat.id,pic)
        #bot.send_photo(message.chat.id, "https://drive.google.com/file/d/1rDcvn1ZkJKrONi6_aT_vWocO17Djm_xs/view?usp=sharing")
        #bot.send_animation(message.chat.id,"https://media.tenor.com/20cy0Nvt87MAAAAS/zindagi-barbaad.gif")
        #bot.send_video(message.chat.id,"https://indianmemetemplates.com/wp-content/uploads/usse-mera-kya-faiyda.mp4")
        #bot.send_photo(message.chat.id,'https://nojoto.com/_next/image?url=https%3A%2F%2Fmedia.nojoto.com%2Fcontent%2Fmedia%2F1722642%2F2020%2F03%2Ffeed%2F7228d29096bfddc8c2c20bf6c8280d2f%2F7228d29096bfddc8c2c20bf6c8280d2f_default.jpg&w=1920&q=75')
        #bot.send_photo(message.chat.id,"https://media.makeameme.org/created/bhai-h-tu.jpg")
        bot.send_message(message.chat.id,"select kar le")
        bot.send_message(message.chat.id,"for first semester type/touch = /1")
        bot.send_message(message.chat.id,"for second semester type /2")
        bot.send_message(message.chat.id,"for thrid semester type /3")
        bot.send_message(message.chat.id,"for fourth semester type /4")
        bot.send_message(message.chat.id,"for five semester type /5")
        bot.send_message(message.chat.id,"for six semester type /6")
        bot.send_message(message.chat.id,"for seven semester type /7")
        bot.send_message(message.chat.id,"for eight semester type /8")
        @bot.message_handler(commands=['1'])
        def first(message):
          bot.send_message(message.chat.id,'https://drive.google.com/file/d/1i-RErMqXRZRXDeXRBT-tYmTrnCRPZUQJ/view?usp=sharing')
          bot.send_message(message.chat.id,'for first semester breif syllabus type /1s')
          @bot.message_handler(commands=['1s'])
          def firstsem(message):
           bot.send_message(message.chat.id,'physics ')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1b_rPUgiHJc2uzmEyYnu1M8dox9e44J4K/view?usp=share_link')
           bot.send_message(message.chat.id,'Mathematics')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1KBfggETDelgSFMROFfSbKK_Re6LMA3-m/view?usp=share_link')
           bot.send_message(message.chat.id,'Basic Electrical Engineering')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/17Ysmv81nMKloGma8M0zDm05Te7hll_AJ/view?usp=share_link')
           bot.send_message(message.chat.id,'Engineering Graphics and Design')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1c5zPAh6yL4hjz-1uo6GWq2jzMEIODL0r/view?usp=share_link')
           bot.send_message(message.chat.id,'Environmental Science')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1CWEj4dPoyev_PbsNpAijUr8foFoTQeMe/view?usp=share_link')
           bot.send_video(message.chat.id,'https://indianmemetemplates.com/wp-content/uploads/emotional-damage.mp4')

        @bot.message_handler(commands=['2'])
        def second(message):
          bot.send_message(message.chat.id,"https://drive.google.com/file/d/1Dtzi9tlnaGCxnzSxs-7SJksGBe8NxIqb/view?usp=sharing",)
          bot.send_message(message.chat.id,'for second semester breif syllabus type /2s')
          @bot.message_handler(commands=['2s'])
          def secondsem(message):
           bot.send_message(message.chat.id,'Chemistry')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1y-VIpIAVcScaREcjBNV0GuIwl-gR9IRl/view?usp=share_link')
           bot.send_message(message.chat.id,'Mathematics II')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1f0qus2WUxfNz64idbwfjuykpOrv9VrYb/view?usp=share_link')
           bot.send_message(message.chat.id,'Programming for Problem Solving')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1KzO_ztYFFCLvTMSHOJhAdHw_qnyiy11J/view?usp=share_link')
           bot.send_message(message.chat.id,'Workshop Practices')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1fiBYivy0j39M4QFW0hLltWZ9o0yw_kwO/view?usp=share_link')
           bot.send_message(message.chat.id,'English')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1QV7S9dfGUiGX_lQriG61STNsGFwk_wBp/view?usp=share_link')
           bot.send_video(message.chat.id,'https://indianmemetemplates.com/wp-content/uploads/emotional-damage.mp4')
        @bot.message_handler(commands=['3'])
        def thrid(message):
          bot.send_message(message.chat.id,"https://drive.google.com/file/d/1E4Y2nXnwffIo2bzZ_KnkZy2oqWYIfBSP/view?usp=sharing")
          bot.send_message(message.chat.id,'for thrid semester breif syllabus type /3s')
          @bot.message_handler(commands=['3s'])
          def thridsem(message):
           bot.send_message(message.chat.id,' Data Structures and Algorithms')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1HSW3cjCoYa7qWHeFhPze37lH-ALwSNVn/view?usp=sharing')
           bot.send_message(message.chat.id,'Software Engineering')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1MhFpKJox9vZ3klPsa5vuROgtuq6_lPmv/view?usp=sharing')
           bot.send_message(message.chat.id,'Discrete Mathematics')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1PTD3QeNfRHPK2yArMb6B-HUf9AyL6AH7/view?usp=share_link')
           bot.send_message(message.chat.id,'Digital Electronics')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1Io13lYbSy_D68FI79p3-G-kqhEnhmvlK/view?usp=sharing,')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1ih-kQIIfDAKblYEFR8gKuBeHJtdHjDR7/view?usp=sharing')
           bot.send_message(message.chat.id,'Analog Electronic Circuits')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1QfSqZKRY8A5qEtKzPhUtL-E5S8ucWjK1/view?usp=share_link')
           bot.send_message(message.chat.id,'Effective Technical Communication')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1K-Hcs3_kREpZ7_ppBm3ucoFORzpjTmyr/view?usp=share_link')
           bot.send_video(message.chat.id,'https://indianmemetemplates.com/wp-content/uploads/emotional-damage.mp4')
        @bot.message_handler(commands=['4'])
        def fourth(message):
          bot.send_message(message.chat.id,"https://drive.google.com/file/d/1P757z7aBpNAeyPspP4KBj60XA888a_eP/view?usp=sharing")
          bot.send_message(message.chat.id,'for fourth semester breif syllabus type /4s')
          @bot.message_handler(commands=['4s'])
          def fourthsem(message,video):
           bot.send_message(message.chat.id,'Computer Organization and Architecture ')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1o-bhe2iEjdP7iGDhmOGN6V9p9I_HhD6K/view?usp=share_link')
           bot.send_message(message.chat.id,' Operating Systems')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1-aOADAxyM7kwwCvNDJjhB5IySS92F3Ad/view?usp=share_link')
           bot.send_message(message.chat.id,'Formal Language and Automata Theory')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1zQAxtpAIN3tcLsX-LTtth_dx8v_27Ols/view?usp=share_link')
           bot.send_message(message.chat.id,'IT Workshop')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/14E7vhoxjN1sNZ8p7sJVfPQjH1fF34SxW/view?usp=share_link')
           bot.send_message(message.chat.id,' Mathematics-III ')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1fP0Rx6iGdcJK-JYKsoMI5AmeiI5YFyxh/view?usp=share_link')
           bot.send_message(message.chat.id,'Organizational Behaviour')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1lfk4j4A5sPon1cN8RDe4529T4gQ_woPB/view?usp=share_link')
           bot.send_message(message.chat.id,'Constitution of India')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1wIUGVqeLnXJuYTj0qHbsp1FtZ9qn4jF5/view?usp=share_link')
           bot.send_message(message.chat.id,'BASICS OF AI AND MACHINE LEARNING')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1iObINxlyxJgQXxOUaYvhHjvof9wTcifO/view?usp=share_link')  
           bot.send_message(message.chat.id,'HUMAN VALUES AND ETHICS')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1G8IAFT5lhwLzlfw7N8A2RAHRd_8mAHyl/view?usp=share_link')
           bot.send_message(message.chat.id,'INDUSTRIAL VISIT-1')
           bot.send_message(message.chat.id,'https://drive.google.com/file/d/1ylcgkr2rDz6HKJm8Mpbz3SidplPtTQt8/view?usp=share_link')
           bot.send_video(message.chat.id,'https://indianmemetemplates.com/wp-content/uploads/emotional-damage.mp4')
        @bot.message_handler(commands=['5'])
        def five(message):
          bot.send_message(message.chat.id,"https://drive.google.com/file/d/10keR2OufUCg19YcP41CDJHy13d-y81YM/view?usp=sharing")
          bot.send_message(message.chat.id,'for five semester breif syllabus type /5s')
          @bot.message_handler(commands=['5s'])
          def fitysem(message):
           bot.send_message(message.chat.id,'Database Management Systems')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,'Design and Analysis of Algorithms')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,'Object Oriented Programming')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,'Signals and Systems')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,'Open Elective-1')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,' Elective-I')
           bot.send_message(message.chat.id,'no file exist')
          # bot.send_message(message.chat.id,'Constitution of India')
          #bot.send_message(message.chat.id,'no file exist')
        @bot.message_handler(commands=['6'])
        def six(message):
          bot.send_message(message.chat.id,"https://drive.google.com/file/d/1SS8PfR_a_V8TtduRnT8SOBxjZr9HNI9H/view?usp=sharing")
        #  bot.send_message(message.chat.id,'for six semester breif syllabus type /6s')
          @bot.message_handler(commands=['6s'])
          def sixsem(message):
           bot.send_message(message.chat.id,'Compiler Design')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,'computer Networks ')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,'Elective-II')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,'Elective-III')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,'Soft-skill and Interpersonal Communication')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,'Aptitude and Reasoning and Online Test')
           bot.send_message(message.chat.id,'no file exist')  
        @bot.message_handler(commands=['7'])
        def seven(message):
          bot.send_message(message.chat.id,"https://drive.google.com/file/d/1XooNJ3wpo0eQR2x3ySfhAAhBDPKJ4UbF/view?usp=sharing")
  #        bot.send_message(message.chat.id,'for seven semester breif syllabus type /7s')
          @bot.message_handler(commands=['7s'])
          def sevensem(message):
           bot.send_message(message.chat.id,'Elective-IV ')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,'Elective-V')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,'Open Elective-II')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,'Biology')
           bot.send_message(message.chat.id,'no file exist')
        @bot.message_handler(commands=['8'])
        def eight(message):
          bot.send_message(message.chat.id,"https://drive.google.com/file/d/1kDMSQVrdckaaaKoHCCOZhGos08HfL_u2/view?usp=sharing")
          bot.send_message(message.chat.id,'for eight semester breif syllabus type /8s')
   #       @bot.message_handler(commands=['8s'])
          def eightsem(message):
           bot.send_message(message.chat.id,'Elective-VI')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,'Open Elective-IV')
           bot.send_message(message.chat.id,'no file exist')
           bot.send_message(message.chat.id,'Open Elective-III')
           bot.send_message(message.chat.id,'no file exist')

@bot.message_handler(commands=['civ'])
def civ(message):
      bot.send_message(message.chat.id,'no file exist')    

@bot.message_handler(commands=['bt'])
def bt(message):
        bot.send_message(message.chat.id,'no file exist')

@bot.message_handler(commands=['mec'])
def mec(message):
       bot.send_message(message.chat.id,'no file exist')

@bot.message_handler(commands=['bba'])

def bba(message):
    bot.send_message(message.chat.id,"click the below link for syllabus")
    file2='https://docs.google.com/document/d/18Lf34dZPfM1g6f2_mKYrvriDRcjDAhjC/edit?usp=sharing&ouid=110928754123184665076&rtpof=true&sd=true'
    file='https://docs.google.com/document/d/1FKhXtq2Qzzv_EkJO3KKDVGawUcR5ippm/edit?usp=sharing&ouid=110928754123184665076&rtpof=true&sd=true'
    bot.send_message(message.chat.id,file)
    bot.send_message(message.chat.id,file2)

@bot.message_handler(commands=['diploma'])

def diploma(message):
    bot.send_message(message.chat.id,"click the below link for syllabus")
    file='sorry there is no link'
    bot.send_message(message.chat.id,file)


print("bot running")

bot.infinity_polling()
