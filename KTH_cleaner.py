with open("Testing/boxing.txt") as f:
    content = f.readlines()

print(content)

out=open('Testing/desc.txt','wt')
for s in content:
    w=s.split()
    for i in range(0,(len(w)-1)//2):
        out.write(w[0]+str(" ")+w[2*i+1]+str(" ")+w[2*i+2]+str("\n"))
