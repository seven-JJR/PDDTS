import os,wmi,subprocess
SysVersion = wmi.WMI()
user=os.getlogin()
from iupdatable.system.hardware import CSProduct
cpu = SysVersion.Win32_Processor()[0].name
inumber = CSProduct.get_identifying_number()
inumber_1 = CSProduct.get_name()
SNnumber = inumber_1 + inumber
hddlist=[]
hdd=SysVersion.Win32_DiskDrive()
for ssd in hdd:
    if 'USB' not in ssd.Model:
        hddlist.append(ssd.Model)

if len(hddlist)==1:
    SSD_info='SSD:'+' '+hddlist[0]
else:
    SSD_info='SSD:'+' '+hddlist[0]+','+hddlist[1]
memorylist=[]
memorys=SysVersion.Win32_PhysicalMemory()
for memory in memorys:
    memorylist.append(memory.Manufacturer)
    memorylist.append(memory.Capacity)
if len(memorylist)==4:
    sizeemory = int(int(memorylist[1]) / 1024 / 1024 / 1024)
    sizeemory_1 = str(sizeemory)
    sizeemory2=int(int(memorylist[3]) / 1024 / 1024 / 1024)
    sizeemory_2 = str(sizeemory2)
    memory_info='Memory:'+' '+memorylist[0]+' '+sizeemory_1+'GB'+' '+'+'+' '+memorylist[2]+' '+sizeemory_2+'GB'
else:
    sizeemory = int(int(memorylist[1]) / 1024 / 1024 / 1024)
    sizeemory_1 = str(sizeemory)
    memory_info = 'Memory:' + ' ' + memorylist[0] + ' ' + sizeemory_1 + 'GB'
bios_ver="BIOS:"+' '+SysVersion.Win32_Bios()[0].Description
x=SysVersion.Win32_Bios()[0].EmbeddedControllerMajorVersion
y=SysVersion.Win32_Bios()[0].EmbeddedControllerMinorVersion
y_1=str(y)
x_1=str(x)
if len(y_1)==1:
    ec=x_1+"."+'0'+y_1
else:
    ec=x_1+"."+y_1
osversion= subprocess.check_output("ver",shell=True)
osversion_1=osversion.decode('utf-8')
with open("C:\\Windows\\modules.log") as f:
    data=f.readlines()
    for line in data:
        if 'Report' in line:
            image=str(line)
image_1=image[:-26]
image_1_1=image_1[9:]
os_ver=osversion_1.replace("\n",'')
os_1=os_ver[33:]
os_v=os_1[:-2]

with open(os.path.join("c:\\Users",user,"Desktop","PDDTS.txt"),"w+") as f1:
     f1.write(
"""Title
[Project][Function][Win10/Win11][FVT1.0]xxxxxxxxxxxxxxx(FR: 0/0 units, 0/0 cycles)

Description
==Contact Information==
Reported by: xxx@@wistron.com
Reviewed by: xxx@wistron.com

==Failure Rate==
Failing System Rate: 0 machines / 0 total machines
Error Rate: 0 errors / 0 total trials

==Symptom + Condition==


==Error Message==
None 

==Pre-test Preparation==
1.Prepare SKU and flash xxBIOS/xxEC/xxME
2.Preload Fenrir2 Win11 FVT1
3.Go to BIOS > Enable OS Optimized > F9 > F10 before OOBE

==Recreation Procedure==
1. Open device manager after OOBE
2. Found xxxxx. ->Problem

==Other information==
None

==Expected Behavior==


==How to Recover==


==Problem Isolation==
A) Unique to a certain system? Yes/No-  No - Not Dependent to EUT
B) Unique to a configuration? Yes/No -  No - Not Dependent on configura 
C) Unique to OS? Yes/No -  No - Issue both happening in Win10 and Win11
D) Unique to a product? Yes/No-  No – Golem Talos AMD/intel also Fail
E) Unique to a current version? Yes/No – Yes – Only fail on 23w BIOS, 22w BIOS pass
F) Common OS Issue Yes/No? - if it is OS issue, need to check other product to confirm whether it is common OS issue.
""")
     f1.close()
with open(os.path.join("c:\\Users",user,"Desktop","PDDTS.txt"),"a") as f2:
    data1=('\nAdditional Description:'+'\n'+'Test Units:'+' '+user+"\n"+"CPU:"+" "+cpu+"\n"+"SN Number:"+' '+SNnumber+'\n'+SSD_info+'\n'+
    memory_info+'\n'+'\n'+"""[S/W]"""+'\n'+bios_ver+'\n'+'EC:'+' '+ec+"\n"+'Preload Image:'+' '+image_1_1+'\n'+"OS Build:"+' '+os_v)
    f2.write(data1)
    f2.close()