import pyautogui as pg
dic = {
    "1"  : "com.blockchainvault",  
    "2"  : "com.blockchainvaulv",                          
    "3"  : "com.blockchainvaulf",              
    "4"  : "com.blockchainvaulg",               
    "5"  : "com.blockchainvaulh",           
    "6"  : "com.blockchainvaule",             
    "7"  : "com.blockchainvauld",               
    "8"  : "com.blockchainvaumu",                
    "9"  : "com.blockchainvaumv",            
    "10" : "com.blockchainvaumw",            
    "11" : "com.blockchainvaump",              
    "12" : "com.blockchainvaumm",                  
    "13" : "com.blockchainvauml",                          
    "14" : "com.blockchainvaumk"                 

}

a = input("Enter your number:\n")

if a in dic:
    pg.write("adb shell monkey -p " + dic.get(a) + " -c android.intent.category.LAUNCHER 60 && adb shell input keyevent 66")
    pg.press('enter')
