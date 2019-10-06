# create letters from voter records
# to support candidates

letterText = " Dear %s,\n \
I would like you to vote for %s \n \
because I think %s is best for \n \
this country. \n \
Sincerely, \n \
%s"

voters = [('Hildegard', 'Hillary Clinton', 'Hillary Clinton', 'Brunhilda'),
          ('Cheech', 'Donald Trump', 'Donald Trump', 'Chong'),
          ('Moe', 'Bernie Sanders', 'Bernie Sanders', 'Jack')]

for voter in voters:
    print(letterText % voter)
    print('\n')

# OUTPUT
'''
==================== RESTART: /home/jorge/csf021a/hwk2.py ====================
 Dear Hildegard,
 I would like you to vote for Hillary Clinton 
 because I think Hillary Clinton is best for 
 this country. 
 Sincerely, 
 Brunhilda


 Dear Cheech,
 I would like you to vote for Donald Trump 
 because I think Donald Trump is best for 
 this country. 
 Sincerely, 
 Chong


 Dear Moe,
 I would like you to vote for Bernie Sanders 
 because I think Bernie Sanders is best for 
 this country. 
 Sincerely, 
 Jack
'''

    
