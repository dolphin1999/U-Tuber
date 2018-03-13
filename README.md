# U-Tuber
Multiple Number of youtube videos and playlist downloader just by one click .


Requirements to run script :-


   python2.7

   Tkinter : 
   
             pip install python-tk
   
             sudo apt-get install python-tk
               
   
   
   pytube :
   
   
             pip install pytube
             
             
             or Download .tar.gz file and install
             


Run :-
      
      python u_Download.py



python3.x

   
  First Install Python3.x if not already installed:
   
            sudo apt-get install python3 
            
            sudo apt-get install python3-pip 

   Tkinter : 
   
             pip install python3-tk
   
             sudo apt-get install python3-tk
               
   
   
   pytube :
   
   
             pip3 install pytube
             
             
             or Download .tar.gz file and install
             


Run :-
      
      python3 u_Download_python3.py


 
    
If running behind proxy add following lines in code

         import urllib2
         proxy = urllib2.ProxyHandler({'http':'<username>:<password>@<proxy>:<port>', 'https':'<username>:<password>@<proxy>:<port>'})
         opener = urllib2.build_opener(proxy)
         urllib2.install_opener(opener)
