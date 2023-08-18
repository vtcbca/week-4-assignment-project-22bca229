#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3 as sq
import datetime


# In[7]:


con = sq.connect("contactmanagementsystem229.db")


# In[8]:


cur = con.cursor()


# In[9]:


cur.execute("""create table if not exists contact
               ( cid int primary key,
                 fname text,
                 lname text,
                 contact number,
                 email text,
                 city text
                 check ( email like '%_@_%._%')
                );""")


# In[10]:


cur.execute("""create table if not exists details_log
                (
                    
                    fname text,
                    lname text,
                    newcontact number,
                    oldcontact number,
                    datetime text,
                    operation text
                    
                )""")


# In[11]:


cur.execute("""create trigger if not exists insertdata
               after insert on contact
               begin
                   insert into details_log
                   values(new.fname,new.lname,new.contact,'NULL',datetime('now'),'insert');
               end;
                   """)


# In[12]:


cur.execute("""create trigger if not exists deletedata
               after delete on contact
               begin
                   insert into details_log
                   values(old.fname,old.lname,'NULL',old.contact,datetime('now'),'delete');
               end;
                   """)


# In[13]:


cur.execute("""create trigger if not exists updatedata
               after update on contact
               begin
                   insert into details_log
                   values(new.fname,new.lname,new.contact,old.contact,datetime('now'),'update');
               end;
                   """)


# In[14]:


def updaterecord(cd):
    newcon=int(input("Enter new Contact Number:"))
    cur.execute(f"Update contact set contact={newcon} where cid={cd};")


# In[15]:


def deleterecord(cd):
    cur.execute(f"delete from contact where cid={cd}")


# In[16]:


def searchrecord(cd):
    cur.execute(f"select * from contact where cid={cd}")
    row=cur.fetchall()
    print(row)


# In[17]:


cur.execute("""insert into contact values
                (1,'rehan','shakh',9377373299,'rehanshekh009@gmail.com','haldharu'),
                (2,'tarun','patil',9034567898,'patiltarun123@gmail.com','surat'),
                (3,'milen','tailor',8970564789,'milen789@gmail.com','vakaner'),
                (4,'rudra','solanki',8976620101,'solanki564@gmail.com','chalthan'),
                (5,'ahmmed','patel',9987120302,'ahmmed123@gmail.com','bodhan');""")


# In[ ]:


updaterecord(2)


# In[ ]:


deleterecord(3)


# In[ ]:


cur.execute("select * from contact")
row=cur.fetchall()
for i in row:
    print(f"\nID:{i[0]}\nFname:{i[1]}\nLname:{i[2]}\nContact:{i[3]}\nEmail:{i[4]}\ncity:{i[5]}")


# In[ ]:


cur.execute("select * from details_log")
row1=cur.fetchall()
print(row1)
for i in row1:
    print(f"\nFname:{i[0]}\nLname:{i[1]}\nNew-contact:{i[2]}\nOld-Contact:{i[3]}\nDatetime:{i[4]}\nOperation:{i[5]}")


# In[ ]:




