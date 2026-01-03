nobel_prize

# year   subject  winner   country category
#
# 1970 Physics  hannes  sweden  scientist
#
# ---

#
# # 1).write a sql query to find the nobel prize winners for the year 1970(return year,subject and winner)
# select year,subject,winner from nobel_prize where year=1970
# # 2).write a sql query to find the nobel prize winner in literature for 1971
# select * from nobel_prize where year=1971 and subject="literature"
# # 3).sql to find the winners in the field of physics since 1978(return winner)
# select winner from nobel_prize where subject="physics" and year>=1978
# # 4)sql query to find the winners in chemistry between 1970 and 1980
# select * from nobel_prize where subject="chemistry" and year between 1970 and 1980
# # 5)sql query to find the details of the winners whose firstname match with string 'Louis'
# select * from nobel_prize where namae like 'Louis%'
# # 6).sql query to find the winners excluding subjects physiology and Economics.
# select * from nobel_prize where subject not in('physiology','economics')
