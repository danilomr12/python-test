class PickingTickets:
    
    @staticmethod
    def max_tickets(tickets: list):
        """_summary_
        1. sort list
        2. iterate from 0 index until integer serie get broken.
        3. When 
        """
        lists = []
        def generate_ticket_list(tickets):
            temp_list = []
            for idx in range(len(tickets)-1):
                current = tickets[idx]
                next = tickets[idx+1]
                if(current == next or next == (current + 1)):
                    temp_list.append(current)
                    if(len(tickets)==idx+2):
                        temp_list.append(next)
                        yield temp_list
                elif(len(temp_list) != 0):
                    temp_list.append(current)
                    yield temp_list
                    temp_list = []
                
            
        tickets.sort()
        generator = generate_ticket_list(tickets)
        for item in generator:
            lists.append(item)
        return lists
    
    
max_tickets = PickingTickets.max_tickets([8, 5, 4, 8, 4, 9, 10,12,12,19,14,22,13])
print([len(x) for x in max_tickets])


