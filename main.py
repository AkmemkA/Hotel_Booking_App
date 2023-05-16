import pandas

hotel_df = pandas.read_csv("hotels.csv", dtype={"id": str})
card_df = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = hotel_df.loc[
            hotel_df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        '''Books the hotel by changing availability to no'''
        hotel_df.loc[hotel_df['id'] == self.hotel_id, "available"] = "no"
        hotel_df.to_csv("hotels.csv", index=False)

    def available(self):
        '''Checks if the hotel is available'''
        availability = hotel_df.loc[
            hotel_df['id'] == self.hotel_id, "available"].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number, expiration, cvc, holder):
        self.number = number
        self.expiration = expiration
        self.holder = holder
        self.cvc = cvc

    def validate(self):
        card_data = {"number": self.number, "expiration": self.expiration,
                     "cvc": self.cvc, "holder": self.holder}
        if card_data in card_df:
            return True
        else:
            return False


print(hotel_df)
hotel_input = input("Enter Hotel's ID: ")
hotel = Hotel(hotel_input)

if hotel.available():
    card_number = input("Enter credit card number: ")
    card_exp_date = input("Enter credit card expiration date (##/##): ")
    cvc_code = input("Enter cvc code:  ")
    card_holder = input("Enter name of cardholder: ").upper()
    credit_card = CreditCard(card_number, card_exp_date, cvc_code, card_holder)
    if credit_card.validate():
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(customer_name=name,
                                               hotel_object=hotel)
        print(reservation_ticket.generate())
    else:
        print("Card is not valid")
else:
    print("Hotel is not free")
