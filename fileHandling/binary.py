with open('1.jpeg','rb') as f:
    with open('copy.png','wb') as wf:
        wf.write(f.read())