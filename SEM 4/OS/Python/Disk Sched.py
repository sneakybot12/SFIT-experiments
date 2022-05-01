class DiskScheduling:
    def __init__(self, headPosition, req):

        self.hp = headPosition
        self.requests = req
        self.n = len(self.requests)
        self.NextCylinder = self.requests[0]
        self.TotalHeadMovement = 0
        self.averageHeadMovement = 0

    def FCFS(self):
        headMovement = []
        for i in range(self.n):
            headMovement.append(abs(self.NextCylinder - self.hp))
            print(f"\t{self.NextCylinder}\tSeeked")
            self.hp = self.NextCylinder
            if i is not self.n - 1:
                self.NextCylinder = self.requests[i + 1]
        self.TotalHeadMovement = sum(headMovement)
        print(f"Total Head Movement: {self.TotalHeadMovement}")
        self.averageHeadMovement = self.TotalHeadMovement / self.n
        print(f"Average Head Movement: {self.averageHeadMovement}")

    def SCAN(self):

        req = self.requests.copy()
        time = 0
        pos = self.hp
        end = 200
        start = 0
        for i in range(pos, end + 1):
            if i in req:
                time += abs(pos - i)
                pos = i
                print(" ", i, " seeked")
                req.remove(i)

        time += abs(pos - end)
        pos = end
        for i in range(end, start - 1, -1):
            if i in req:
                time += abs(pos - i)
                # print(time)
                pos = i
                print(" ", i, " seeked")
                req.remove(i)
        self.TotalHeadMovement = time
        print(f"Total Head Movement: {self.TotalHeadMovement}")
        self.averageHeadMovement = self.TotalHeadMovement / self.n
        print(f"Average Head Movement: {self.averageHeadMovement}")


requests = list(map(int, input("Enter the requests :").strip().split()))
hp = int(input("Enter Starting Head Position : "))
d = DiskScheduling(hp, requests)
choice = 0
while choice != 3:
    choice = int(input("1. FCFS\t2. SCAN\t3. EXIT : "))
    if choice == 1:
        d.FCFS()
    if choice == 2:
        d.SCAN()
    if choice == 3:
        break
