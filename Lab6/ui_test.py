from pywinauto import application

app = application.Application()

app.start_('C:\Users\Aaron\Documents\CST-236\sharptona.exe')



#Requirement #0002
print ("\nRequirement #0002")
print app.sharpTona['Question:'].IsEnabled()
print app.sharpTona['Answer:'].IsEnabled()

#Requirement #0003, #0006
print ("\nRequirement #0003, #0006")
app.sharpTona['Question:Edit'].TypeKeys('Who am I?', with_spaces=True)
app.sharpTona['Ask'].Click()
print app.sharpTona['Answer:Edit'].Texts()[0]

app.sharpTona['Question:Edit'].Select()

app.sharpTona.Close()

#requirement #0004
print ("\nRequirement #0004")
app.start_('C:\Users\Aaron\Documents\CST-236\sharptona.exe')
app.sharpTona['Question:Edit'].TypeKeys('What is the answer to everything?', with_spaces=True)
app.sharpTona['Ask'].Click()
print app.sharpTona['Answer:Edit'].Texts()[0]
app.sharpTona.Close()

#requirement #0005
print ("\nRequirement #0005")
app.start_('C:\Users\Aaron\Documents\CST-236\sharptona.exe')
print app.sharpTona['Teach'].IsEnabled()
print app.sharpTona['Correct'].IsEnabled()
app.sharpTona.Close()

#requirement #0007
print ("\nRequirement #0007")
app.start_('C:\Users\Aaron\Documents\CST-236\sharptona.exe')
app.sharpTona['Ask'].Click()
print app.sharpTona['Answer:Edit'].Texts()[0]
app.sharpTona.Close()

#requirement #0008
print ("\nRequirement #0008")
app.start_('C:\Users\Aaron\Documents\CST-236\sharptona.exe')
app.sharpTona['Question:Edit'].TypeKeys('What is the answer to everything?', with_spaces=True)
app.sharpTona['Ask'].Click()
print app.sharpTona['Answer:Edit'].Texts()[0]
print app.sharpTona['Answer:Edit'].IsEnabled()
app.sharpTona.Close()


#requirement #0009
print ("\nRequirement #0009")
app.start_('C:\Users\Aaron\Documents\CST-236\sharptona.exe')
app.sharpTona['Question:Edit'].TypeKeys('What is the answer to everything?', with_spaces=True)
app.sharpTona['Ask'].Click()

app.sharpTona['Answer:Edit'].TypeKeys('Error: Cannot compute infinity (everything=infinity)', with_spaces=True)
app.sharpTona['Correct'].Click()
print app.sharpTona['Answer:Edit'].IsEnabled()
print app.sharpTona['Teach'].IsEnabled()
print app.sharpTona['Correct'].IsEnabled()
app.sharpTona.Close()

#requirement #0010, #0011
print ("\nRequirement #0010, #0011")
app.start_('C:\Users\Aaron\Documents\CST-236\sharptona.exe')
app.sharpTona['Question:Edit'].TypeKeys('What is your name?', with_spaces=True)
app.sharpTona['Ask'].Click()

print app.sharpTona['Answer:Edit'].Texts()[0]
print app.sharpTona['Teach'].IsEnabled()

app.sharpTona['Teach'].Click()
print app.sharpTona['Answer:Edit'].IsEnabled()
print app.sharpTona['Teach'].IsEnabled()
print app.sharpTona['Correct'].IsEnabled()

app.sharpTona.Close()
