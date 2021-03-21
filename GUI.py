from tkinter import *
import paramiko
from getpass import getpass
import time
from time import sleep


app = Tk()

####################################################
app.title("MPLS configureation wizard")#############
app.geometry('750x400')#############################
####################################################
##the loopback interface
def LoopBack(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    LoopBack = Toplevel(app) 
    LoopBack.geometry("1000x400")
    


    def Submit():
        remote_conn_pre=paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(sship_text.get(), port=22, username=sshusr_text.get(), password=sshpas_text.get(), look_for_keys=False, allow_agent=False)
        remote_conn = remote_conn_pre.invoke_shell()
        sleep(0.5) 
        remote_conn.send("en\n")
        sleep(0.5)
        remote_conn.send(sshpas_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("conf t\n")
        sleep(0.1)
        remote_conn.send("interface loopback "+ intnum_text.get()+"\n")
        sleep(0.1)
        remote_conn.send("ip address "+loip_text.get()+ " " + lomask_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("ip ospf "+ospft_text.get()+" area "+ospfa_text.get()+"\n")
        sleep(0.1)



        


    









    # sets the title of the 
    # Toplevel widget 
    LoopBack.title("Loopback configuration") 









    ##############################################################
    ##############################################################
    sship_text = StringVar()    
    sship_label = Label(LoopBack, text='Router SSH IP', pady=20)
    sship_label.grid(row=0, column=0, sticky=W)
    sship_entry = Entry(LoopBack, textvariable=sship_text)
    sship_entry.grid(row=0, column=1)
    ##############################################################
    ##############################################################
    sshusr_text = StringVar()    
    sshusr_label = Label(LoopBack, text='Router SSH username', pady=20)
    sshusr_label.grid(row=0, column=2, sticky=W)
    sshusr_entry = Entry(LoopBack, textvariable=sshusr_text)
    sshusr_entry.grid(row=0, column=3)
    ##############################################################
    ##############################################################
    sshpas_text = StringVar()    
    sshpas_label = Label(LoopBack, text='Router SSH password', pady=20)
    sshpas_label.grid(row=0, column=4, sticky=W)
    sshpas_entry = Entry(LoopBack, textvariable=sshpas_text)
    sshpas_entry.grid(row=0, column=5)
    ##############################################################
    ##############################################################
    intnum_text = StringVar()    
    intnum_label = Label(LoopBack, text='Interface Number', pady=20)
    intnum_label.grid(row=1, column=0, sticky=W)
    intnum_entry = Entry(LoopBack, textvariable=intnum_text)
    intnum_entry.grid(row=1, column=1)
    ##############################################################
    ##############################################################
    loip_text = StringVar()    
    loip_label = Label(LoopBack, text='Enter the interface IP', pady=20)
    loip_label.grid(row=2, column=0, sticky=W)
    loip_entry = Entry(LoopBack, textvariable=loip_text)
    loip_entry.grid(row=2, column=1)
    ##############################################################
    ##############################################################
    lomask_text = StringVar()    
    lomask_label = Label(LoopBack, text='Enter the interface mask', pady=20,padx=20)
    lomask_label.grid(row=2, column=2, sticky=W)
    lomask_entry = Entry(LoopBack, textvariable=lomask_text)
    lomask_entry.grid(row=2, column=3)
    ##############################################################
    ##############################################################
    ospft_text = StringVar()    
    ospft_label = Label(LoopBack, text='Enter the OSPF type', pady=20)
    ospft_label.grid(row=4, column=0, sticky=W)
    ospft_entry = Entry(LoopBack, textvariable=ospft_text)
    ospft_entry.grid(row=4, column=1)
    ##############################################################
    ##############################################################
    ospfa_text = StringVar()    
    ospfa_label = Label(LoopBack, text='Enter the OSPF area', pady=20,padx=20)
    ospfa_label.grid(row=4, column=2, sticky=W)
    ospfa_entry = Entry(LoopBack, textvariable=ospfa_text)
    ospfa_entry.grid(row=4, column=3)
    ##############################################################
    ##############################################################
    
    
    
    

    submit_btn = Button(LoopBack, text='Submit', width=20,command = Submit)
    submit_btn.grid(row=7, column=7, pady=20, padx=20)

    


##the interfaces and ospf
def intandospf():  
    intandospf = Toplevel(app) 
    intandospf.geometry("1000x400")
    intandospf.title("interfaces and the IP's and OSPF")
    def Submit():
        remote_conn_pre=paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(sship_text.get(), port=22, username=sshusr_text.get(), password=sshpas_text.get(), look_for_keys=False, allow_agent=False)
        remote_conn = remote_conn_pre.invoke_shell()
        sleep(0.5) 
        remote_conn.send("en\n")
        sleep(0.5)
        remote_conn.send(sshpas_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("conf t\n")
        sleep(0.1)
        remote_conn.send("interface "+intnum_text.get()+"\n")
        sleep(0.1)
        remote_conn.send("ip add "+loip_text.get()+ " " + lomask_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("no shutdown\n")
        sleep(0.9)
        remote_conn.send("ip ospf "+ospft_text.get()+" area "+ospfa_text.get()+"\n")
        sleep(0.1)





    ##############################################################
    ##############################################################
    sship_text = StringVar()    
    sship_label = Label(intandospf, text='Router SSH IP', pady=20)
    sship_label.grid(row=0, column=0, sticky=W)
    sship_entry = Entry(intandospf, textvariable=sship_text)
    sship_entry.grid(row=0, column=1)
    ##############################################################
    ##############################################################
    sshusr_text = StringVar()    
    sshusr_label = Label(intandospf, text='Router SSH username', pady=20)
    sshusr_label.grid(row=0, column=2, sticky=W)
    sshusr_entry = Entry(intandospf, textvariable=sshusr_text)
    sshusr_entry.grid(row=0, column=3)
    ##############################################################
    ##############################################################
    sshpas_text = StringVar()    
    sshpas_label = Label(intandospf, text='Router SSH password', pady=20)
    sshpas_label.grid(row=0, column=4, sticky=W)
    sshpas_entry = Entry(intandospf, textvariable=sshpas_text)
    sshpas_entry.grid(row=0, column=5)
    ##############################################################
    ##############################################################
    intnum_text = StringVar()    
    intnum_label = Label(intandospf, text='Interface Number', pady=20)
    intnum_label.grid(row=1, column=0, sticky=W)
    intnum_entry = Entry(intandospf, textvariable=intnum_text)
    intnum_entry.grid(row=1, column=1)
    ##############################################################
    ##############################################################
    loip_text = StringVar()    
    loip_label = Label(intandospf, text='Enter the interface IP', pady=20)
    loip_label.grid(row=2, column=0, sticky=W)
    loip_entry = Entry(intandospf, textvariable=loip_text)
    loip_entry.grid(row=2, column=1)
    ##############################################################
    ##############################################################
    lomask_text = StringVar()    
    lomask_label = Label(intandospf, text='Enter the interface mask', pady=20,padx=20)
    lomask_label.grid(row=2, column=2, sticky=W)
    lomask_entry = Entry(intandospf, textvariable=lomask_text)
    lomask_entry.grid(row=2, column=3)
    ##############################################################
    ##############################################################
    ospft_text = StringVar()    
    ospft_label = Label(intandospf, text='Enter the OSPF type', pady=20)
    ospft_label.grid(row=4, column=0, sticky=W)
    ospft_entry = Entry(intandospf, textvariable=ospft_text)
    ospft_entry.grid(row=4, column=1)
    ##############################################################
    ##############################################################
    ospfa_text = StringVar()    
    ospfa_label = Label(intandospf, text='Enter the OSPF area', pady=20,padx=20)
    ospfa_label.grid(row=4, column=2, sticky=W)
    ospfa_entry = Entry(intandospf, textvariable=ospfa_text)
    ospfa_entry.grid(row=4, column=3)
    ##############################################################
    ##############################################################
    submit_btn = Button(intandospf, text='Submit', width=20,command = Submit)
    submit_btn.grid(row=7, column=7, pady=20, padx=20)
     



##the MPLS Interface
def MPLSand():  
    MPLSand = Toplevel(app) 
    MPLSand.geometry("1000x400")
    MPLSand.title("MPLS configuration")
    def Submit():
        remote_conn_pre=paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(sship_text.get(), port=22, username=sshusr_text.get(), password=sshpas_text.get(), look_for_keys=False, allow_agent=False)
        remote_conn = remote_conn_pre.invoke_shell()
        sleep(0.5) 
        remote_conn.send("en\n")
        sleep(0.5)
        remote_conn.send(sshpas_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("conf t\n")
        sleep(0.1)
        remote_conn.send("router ospf "+OSPFnum_text.get()+"\n")
        sleep(0.1)
        remote_conn.send("mpls ldp autoconfig\n")
        sleep(0.1)




    ##############################################################
    ##############################################################
    sship_text = StringVar()    
    sship_label = Label(MPLSand, text='Router SSH IP', pady=20)
    sship_label.grid(row=0, column=0, sticky=W)
    sship_entry = Entry(MPLSand, textvariable=sship_text)
    sship_entry.grid(row=0, column=1)
    ##############################################################
    ##############################################################
    sshusr_text = StringVar()    
    sshusr_label = Label(MPLSand, text='Router SSH username', pady=20)
    sshusr_label.grid(row=0, column=2, sticky=W)
    sshusr_entry = Entry(MPLSand, textvariable=sshusr_text)
    sshusr_entry.grid(row=0, column=3)
    ##############################################################
    ##############################################################
    sshpas_text = StringVar()    
    sshpas_label = Label(MPLSand, text='Router SSH password', pady=20)
    sshpas_label.grid(row=0, column=4, sticky=W)
    sshpas_entry = Entry(MPLSand, textvariable=sshpas_text)
    sshpas_entry.grid(row=0, column=5)
    ##############################################################
    ##############################################################
    OSPFnum_text = StringVar()    
    OSPFnum_label = Label(MPLSand, text='OSPF type', pady=20)
    OSPFnum_label.grid(row=1, column=0, sticky=W)
    OSPFnum_entry = Entry(MPLSand, textvariable=OSPFnum_text)
    OSPFnum_entry.grid(row=1, column=1)
    ##############################################################
    ##############################################################
    submit_btn = Button(MPLSand, text='Submit', width=20,command = Submit)
    submit_btn.grid(row=7, column=7, pady=20, padx=20)
    
     


def BGPm():  
    BGPm = Toplevel(app) 
    BGPm.geometry("1000x400")
    BGPm.title("BGP and MPLS configure")
    def Submit():
        remote_conn_pre=paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(sship_text.get(), port=22, username=sshusr_text.get(), password=sshpas_text.get(), look_for_keys=False, allow_agent=False)
        remote_conn = remote_conn_pre.invoke_shell()
        sleep(0.5) 
        remote_conn.send("en\n")
        sleep(0.5)
        remote_conn.send(sshpas_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("conf t\n")
        sleep(0.1)
        remote_conn.send("router bgp "+bgpn_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("neighbor "+bgpne_text.get()+" remote-as "+remote_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("neighbor "+bgpne_text.get()+ " update-source Loopback0\n")
        sleep(0.5)
        remote_conn.send("no auto-summary\n")
        sleep(0.5)
        remote_conn.send("!\n")
        sleep(0.5)
        remote_conn.send("address-family vpnv4\n")
        sleep(0.5)
        remote_conn.send("neighbor "+bgpne_text.get()+" activate\n")
        sleep(0.5)




    ##############################################################
    ##############################################################
    sship_text = StringVar()    
    sship_label = Label(BGPm, text='Router SSH IP', pady=20)
    sship_label.grid(row=0, column=0, sticky=W)
    sship_entry = Entry(BGPm, textvariable=sship_text)
    sship_entry.grid(row=0, column=1)
    ##############################################################
    ##############################################################
    sshusr_text = StringVar()    
    sshusr_label = Label(BGPm, text='Router SSH username', pady=20)
    sshusr_label.grid(row=0, column=2, sticky=W)
    sshusr_entry = Entry(BGPm, textvariable=sshusr_text)
    sshusr_entry.grid(row=0, column=3)
    ##############################################################
    ##############################################################
    sshpas_text = StringVar()    
    sshpas_label = Label(BGPm, text='Router SSH password', pady=20)
    sshpas_label.grid(row=0, column=4, sticky=W)
    sshpas_entry = Entry(BGPm, textvariable=sshpas_text)
    sshpas_entry.grid(row=0, column=5)
    ##############################################################
    ##############################################################
    bgpn_text = StringVar()    
    bgpn_label = Label(BGPm, text='enter BGP number', pady=20)
    bgpn_label.grid(row=1, column=0, sticky=W)
    bgpn_entry = Entry(BGPm, textvariable=bgpn_text)
    bgpn_entry.grid(row=1, column=1)
    ##############################################################
    ##############################################################
    bgpne_text = StringVar()    
    bgpne_label = Label(BGPm, text='BGP neighbor address', pady=20)
    bgpne_label.grid(row=2, column=0, sticky=W)
    bgpne_entry = Entry(BGPm, textvariable=bgpne_text)
    bgpne_entry.grid(row=2, column=1)
    ##############################################################
    ##############################################################
    remote_text = StringVar()    
    remote_label = Label(BGPm, text='set remote as number', pady=20,padx=20)
    remote_label.grid(row=2, column=2, sticky=W)
    remote_entry = Entry(BGPm, textvariable=remote_text)
    remote_entry.grid(row=2, column=3)
    ##############################################################
    ##############################################################
    submit_btn = Button(BGPm, text='Submit', width=20,command = Submit)
    submit_btn.grid(row=7, column=7, pady=20, padx=20)





def edgens():  
    edgens = Toplevel(app) 
    edgens.geometry("1000x400")
    edgens.title("edge routers and assosiated routers configure")
    def Submit():
        remote_conn_pre=paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(sship_text.get(), port=22, username=sshusr_text.get(), password=sshpas_text.get(), look_for_keys=False, allow_agent=False)
        remote_conn = remote_conn_pre.invoke_shell()
        sleep(0.5) 
        remote_conn.send("en\n")
        sleep(0.5)
        remote_conn.send(sshpas_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("conf t\n")
        sleep(0.1)
        remote_conn.send("interface "+intnum_text.get()+"\n")
        sleep(0.1)
        remote_conn.send("ip add "+loip_text.get()+ " " + lomask_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("no shutdown\n")
        sleep(0.9)
        if ospfyn_text.get() == "yes":
            remote_conn.send("ip ospf "+ospft_text.get()+" area "+ospfa_text.get()+"\n")
            sleep(0.1)

        





    ##############################################################
    ##############################################################
    sship_text = StringVar()    
    sship_label = Label(edgens, text='Router SSH IP', pady=20)
    sship_label.grid(row=0, column=0, sticky=W)
    sship_entry = Entry(edgens, textvariable=sship_text)
    sship_entry.grid(row=0, column=1)
    ##############################################################
    ##############################################################
    sshusr_text = StringVar()    
    sshusr_label = Label(edgens, text='Router SSH username', pady=20)
    sshusr_label.grid(row=0, column=2, sticky=W)
    sshusr_entry = Entry(edgens, textvariable=sshusr_text)
    sshusr_entry.grid(row=0, column=3)
    ##############################################################
    ##############################################################
    sshpas_text = StringVar()    
    sshpas_label = Label(edgens, text='Router SSH password', pady=20)
    sshpas_label.grid(row=0, column=4, sticky=W)
    sshpas_entry = Entry(edgens, textvariable=sshpas_text)
    sshpas_entry.grid(row=0, column=5)
    ##############################################################
    ##############################################################
    intnum_text = StringVar()    
    intnum_label = Label(edgens, text='Interface name', pady=20)
    intnum_label.grid(row=1, column=0, sticky=W)
    intnum_entry = Entry(edgens, textvariable=intnum_text)
    intnum_entry.grid(row=1, column=1)
    ##############################################################
    ##############################################################
    loip_text = StringVar()    
    loip_label = Label(edgens, text='Enter the interface IP', pady=20)
    loip_label.grid(row=2, column=0, sticky=W)
    loip_entry = Entry(edgens, textvariable=loip_text)
    loip_entry.grid(row=2, column=1)
    ##############################################################
    ##############################################################
    lomask_text = StringVar()    
    lomask_label = Label(edgens, text='Enter the interface mask', pady=20,padx=20)
    lomask_label.grid(row=2, column=2, sticky=W)
    lomask_entry = Entry(edgens, textvariable=lomask_text)
    lomask_entry.grid(row=2, column=3)
    ##############################################################
    ##############################################################
    ospfyn_text = StringVar()    
    ospfyn_label = Label(edgens, text='do you want to configure OSPF(yes/no)', pady=20,)
    ospfyn_label.grid(row=3, column=0, sticky=W)
    ospfyn_entry = Entry(edgens, textvariable=ospfyn_text)
    ospfyn_entry.grid(row=3, column=1)
    ##############################################################
    ##############################################################
    ospft_text = StringVar()    
    ospft_label = Label(edgens, text='Enter the OSPF type', pady=20)
    ospft_label.grid(row=4, column=0, sticky=W)
    ospft_entry = Entry(edgens, textvariable=ospft_text)
    ospft_entry.grid(row=4, column=1)
    ##############################################################
    ##############################################################
    ospfa_text = StringVar()    
    ospfa_label = Label(edgens, text='Enter the OSPF area', pady=20,padx=20)
    ospfa_label.grid(row=4, column=2, sticky=W)
    ospfa_entry = Entry(edgens, textvariable=ospfa_text)
    ospfa_entry.grid(row=4, column=3)
    ##############################################################
    ##############################################################
    submit_btn = Button(edgens, text='Submit', width=20,command = Submit)
    submit_btn.grid(row=7, column=5, pady=20, padx=20)




def vrf():  
    vrf = Toplevel(app) 
    vrf.geometry("1000x400")
    vrf.title("VRF setup")
    def Submit():
        remote_conn_pre=paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(sship_text.get(), port=22, username=sshusr_text.get(), password=sshpas_text.get(), look_for_keys=False, allow_agent=False)
        remote_conn = remote_conn_pre.invoke_shell()
        sleep(0.5) 
        remote_conn.send("en\n")
        sleep(0.5)
        remote_conn.send(sshpas_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("conf t\n")
        sleep(0.1)
        remote_conn.send("ip vrf "+vrfn_text.get()+"\n")
        sleep(0.1)
        remote_conn.send("rd 4:4\n")
        sleep(0.1)
        remote_conn.send("route-target both 4:4\n")
        sleep(0.1)
        remote_conn.send("exit\n")
        sleep(0.1)
        remote_conn.send("int "+vrfint_text.get()+"\n")
        sleep(0.1)
        remote_conn.send("ip vrf forwarding "+vrfn_text.get()+"\n")
        sleep(0.1)
        remote_conn.send("ip add "+vrfintip_text.get()+" "+vrfintm_text.get()+"\n")
        sleep(0.1)
        remote_conn.send("ip ospf "+ospft_text.get()+ " area "+ospfa_text.get()+"\n")
        sleep(0.1)

        





    ##############################################################
    ##############################################################
    sship_text = StringVar()    
    sship_label = Label(vrf, text='Router SSH IP', pady=20)
    sship_label.grid(row=0, column=0, sticky=W)
    sship_entry = Entry(vrf, textvariable=sship_text)
    sship_entry.grid(row=0, column=1)
    ##############################################################
    ##############################################################
    sshusr_text = StringVar()    
    sshusr_label = Label(vrf, text='Router SSH username', pady=20)
    sshusr_label.grid(row=0, column=2, sticky=W)
    sshusr_entry = Entry(vrf, textvariable=sshusr_text)
    sshusr_entry.grid(row=0, column=3)
    ##############################################################
    ##############################################################
    sshpas_text = StringVar()    
    sshpas_label = Label(vrf, text='Router SSH password', pady=20)
    sshpas_label.grid(row=0, column=4, sticky=W)
    sshpas_entry = Entry(vrf, textvariable=sshpas_text)
    sshpas_entry.grid(row=0, column=5)
    ##############################################################
    ##############################################################
    vrfn_text = StringVar()    
    vrfn_label = Label(vrf, text='VRF name', pady=20)
    vrfn_label.grid(row=1, column=0, sticky=W)
    vrfn_entry = Entry(vrf, textvariable=vrfn_text)
    vrfn_entry.grid(row=1, column=1)
    ##############################################################
    ##############################################################
    vrfint_text = StringVar()    
    vrfint_label = Label(vrf, text='Enter the interface name to reapply config', pady=20)
    vrfint_label.grid(row=2, column=0, sticky=W)
    vrfint_entry = Entry(vrf, textvariable=vrfint_text)
    vrfint_entry.grid(row=2, column=1)
    ##############################################################
    ##############################################################
    vrfintip_text = StringVar()    
    vrfintip_label = Label(vrf, text='Enter the interface ip', pady=20)
    vrfintip_label.grid(row=3, column=0, sticky=W)
    vrfintip_entry = Entry(vrf, textvariable=vrfintip_text)
    vrfintip_entry.grid(row=3, column=1)
    ##############################################################
    ##############################################################
    vrfintm_text = StringVar()    
    vrfintm_label = Label(vrf, text='enter the interface mask', pady=20,)
    vrfintm_label.grid(row=3, column=2, sticky=W)
    vrfintm_entry = Entry(vrf, textvariable=vrfintm_text)
    vrfintm_entry.grid(row=3, column=3)
    ##############################################################
    ##############################################################
    ospft_text = StringVar()    
    ospft_label = Label(vrf, text='Enter the OSPF type', pady=20)
    ospft_label.grid(row=4, column=0, sticky=W)
    ospft_entry = Entry(vrf, textvariable=ospft_text)
    ospft_entry.grid(row=4, column=1)
    ##############################################################
    ##############################################################
    ospfa_text = StringVar()    
    ospfa_label = Label(vrf, text='Enter the OSPF area', pady=20,padx=20)
    ospfa_label.grid(row=4, column=2, sticky=W)
    ospfa_entry = Entry(vrf, textvariable=ospfa_text)
    ospfa_entry.grid(row=4, column=3)
    ##############################################################
    ##############################################################
    submit_btn = Button(vrf, text='Submit', width=20,command = Submit)
    submit_btn.grid(row=7, column=5, pady=20, padx=20)


def rede():  
    rede = Toplevel(app) 
    rede.geometry("1000x400")
    rede.title("BGP and OSPF Redistribute")
    def Submit():
        remote_conn_pre=paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(sship_text.get(), port=22, username=sshusr_text.get(), password=sshpas_text.get(), look_for_keys=False, allow_agent=False)
        remote_conn = remote_conn_pre.invoke_shell()
        sleep(0.5) 
        remote_conn.send("en\n")
        sleep(0.5)
        remote_conn.send(sshpas_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("conf t\n")
        sleep(0.1)
        remote_conn.send("router bgp "+bgpn_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("address-family ipv4 vrf "+vrfname_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("redistribute ospf "+ospfnum_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("ip vrf "+vrfname_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("ip vrf "+vrfname_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("exit\n")
        sleep(0.5)
        remote_conn.send("exit\n")
        sleep(0.5)
        remote_conn.send("router ospf "+ospfnum2_text.get()+"\n")
        sleep(0.5)
        remote_conn.send("redistribute bgp "+bgpn_text.get()+" subnets\n" )

        





    ##############################################################
    ##############################################################
    sship_text = StringVar()    
    sship_label = Label(rede, text='Router SSH IP', pady=20)
    sship_label.grid(row=0, column=0, sticky=W)
    sship_entry = Entry(rede, textvariable=sship_text)
    sship_entry.grid(row=0, column=1)
    ##############################################################
    ##############################################################
    sshusr_text = StringVar()    
    sshusr_label = Label(rede, text='Router SSH username', pady=20)
    sshusr_label.grid(row=0, column=2, sticky=W)
    sshusr_entry = Entry(rede, textvariable=sshusr_text)
    sshusr_entry.grid(row=0, column=3)
    ##############################################################
    ##############################################################
    sshpas_text = StringVar()    
    sshpas_label = Label(rede, text='Router SSH password', pady=20)
    sshpas_label.grid(row=0, column=4, sticky=W)
    sshpas_entry = Entry(rede, textvariable=sshpas_text)
    sshpas_entry.grid(row=0, column=5)
    ##############################################################
    ##############################################################
    bgpn_text = StringVar()    
    bgpn_label = Label(rede, text='enter BGP number', pady=20)
    bgpn_label.grid(row=1, column=0, sticky=W)
    bgpn_entry = Entry(rede, textvariable=bgpn_text)
    bgpn_entry.grid(row=1, column=1)
    ##############################################################
    ##############################################################
    vrfname_text = StringVar()    
    vrfname_label = Label(rede, text='Enter VRF name', pady=20)
    vrfname_label.grid(row=2, column=0, sticky=W)
    vrfname_entry = Entry(rede, textvariable=vrfname_text)
    vrfname_entry.grid(row=2, column=1)
    ##############################################################
    ##############################################################
    ospfnum_text = StringVar()    
    ospfnum_label = Label(rede, text='Enter OSPF number', pady=20)
    ospfnum_label.grid(row=3, column=0, sticky=W)
    ospfnum_entry = Entry(rede, textvariable=ospfnum_text)
    ospfnum_entry.grid(row=3, column=1)
    ##############################################################
    ##############################################################
    ospfnum2_text = StringVar()    
    ospfnum2_label = Label(rede, text='Enter the second OSPF number', pady=20)
    ospfnum2_label.grid(row=3, column=2, sticky=W)
    ospfnum2_entry = Entry(rede, textvariable=ospfnum2_text)
    ospfnum2_entry.grid(row=3, column=3)
    ##############################################################
    ##############################################################
    submit_btn = Button(rede, text='Submit', width=20,command = Submit)
    submit_btn.grid(row=7, column=5, pady=20, padx=20)







####################################################################
loop_btn = Button(app, text='Loopback and OSPF configure', width=40,command = LoopBack)
loop_btn.grid(row=0, column=0, pady=20, padx=20)
####################################################################
interface_btn = Button(app, text="interfaces and the IP's and OSPF", width=40,command = intandospf)
interface_btn.grid(row=0, column=1, pady=20, padx=20)
####################################################################
mpls_btn = Button(app, text="MPLS configuration", width=40,command = MPLSand)
mpls_btn.grid(row=1, column=0, pady=20, padx=20)
####################################################################
add_btn = Button(app, text="BGP and MPLS configure", width=40,command = BGPm)
add_btn.grid(row=1, column=1, pady=20, padx=20)
####################################################################
add_btn = Button(app, text="edge routers and assosiated routers configure", width=40,command=edgens)
add_btn.grid(row=2, column=0, pady=20, padx=20)
####################################################################
add_btn = Button(app, text="VRF setup", width=40,command = vrf)
add_btn.grid(row=2, column=1, pady=20, padx=20)
####################################################################
add_btn = Button(app, text="BGP and OSPF Redistribute", width=40,command = rede)
add_btn.grid(row=3, column=0, pady=20, padx=20)








app.mainloop()
