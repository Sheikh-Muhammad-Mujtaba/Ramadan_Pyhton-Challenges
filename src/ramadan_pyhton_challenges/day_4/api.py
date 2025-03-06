from fastapi import FastAPI
import random


app = FastAPI()


# two simple get endpoints
# 1 side hustles
# 2. money quotes

side_hustles = [
    "Blogging - Create content and earn through ads and sponsorships.",
    "Freelancing - Start selling your skills (e.g., writing, design, coding).",
    "YouTube Channel - Create videos and monetize through ads and sponsors.",
    "Dropshipping - Sell products online without holding inventory.",
    "Affiliate Marketing - Promote products and earn commissions for sales.",
    "Online Tutoring - Teach subjects or skills you’re knowledgeable in.",
    "Social Media Management - Manage accounts for businesses or influencers.",
    "Print-on-Demand - Design and sell custom merchandise (e.g., T-shirts, mugs).",
    "Virtual Assistant - Provide administrative support to businesses or entrepreneurs.",
    "Stock Photography - Sell your photos on platforms like Shutterstock or Adobe Stock.",
    "Podcasting - Start a podcast and earn through sponsorships and ads.",
    "E-book Writing - Write and sell e-books on platforms like Amazon Kindle.",
    "Online Courses - Create and sell courses on platforms like Udemy or Teachable.",
    "Pet Sitting/Dog Walking - Offer pet care services in your local area.",
    "Ridesharing - Drive for companies like Uber or Lyft.",
    "Delivery Services - Deliver food or packages for companies like DoorDash or Postmates.",
    "Handmade Crafts - Sell handmade items on Etsy or at local markets.",
    "Flipping Items - Buy and resell items for profit (e.g., thrift store finds).",
    "Fitness Coaching - Offer personal training or fitness advice online or in-person.",
    "Real Estate Photography - Take professional photos for real estate listings."
]

money_quotes = [
    "Warren Buffett - 'Do not save what is left after spending, but spend what is left after saving.'",
    "Robert Kiyosaki - 'It’s not how much money you make, but how much money you keep, how hard it works for you, and how many generations you keep it for.'",
    "Dave Ramsey - 'You must gain control over your money or the lack of it will forever control you.'",
    "Benjamin Franklin - 'An investment in knowledge pays the best interest.'",
    "Steve Jobs - 'Your time is limited, don’t waste it living someone else’s life. Don’t be trapped by dogma, which is living with the results of other people’s thinking.'",
    "Maya Angelou - 'When you know better, you do better.'",
    "Mark Cuban - 'It doesn’t matter how many times you fail. You only have to be right once, and then everyone can tell you that you are an overnight success.'",
    "Oprah Winfrey - 'The more you praise and celebrate your life, the more there is in life to celebrate.'",
    "Tony Robbins - 'The path to success is to take massive, determined action.'",
    "Bill Gates - 'If you are born poor, it’s not your mistake. But if you die poor, it’s your mistake.'",
    "John D. Rockefeller - 'The secret to success is to do the common things uncommonly well.'",
    "Jim Rohn - 'Formal education will make you a living; self-education will make you a fortune.'",
    "Thomas Edison - 'Opportunity is missed by most people because it is dressed in overalls and looks like work.'",
    "Henry Ford - 'Whether you think you can or you think you can’t, you’re right.'",
    "Elon Musk - 'When something is important enough, you do it even if the odds are not in your favor.'",
    "Aristotle - 'Money is a guarantee that we may have what we want in the future. Though we need nothing at the moment, it insures the possibility of satisfying a new desire when it arises.'",
    "Grant Cardone - 'The only way you will ever permanently take control of your financial life is to dig deep and fix the root problem.'",
    "Suze Orman - 'A big part of financial freedom is having your heart and mind free from worry about the what-ifs of life.'",
    "Napoleon Hill - 'If you cannot do great things, do small things in a great way.'",
    "Chris Hogan - 'Every dollar you spend is a vote for the kind of world you want.'"
]


@app.get("/side-hustles")
def get_side_hustles(apiKey: str):
    if apiKey != "1234567890": # checks if the API key is valid
        return { "error": "Invalid API Key" }
    return { "side_hustle": random.choice(side_hustles) } # returns random side hustles

@app.post("/side-hustles")
def post_side_hustles(apiKey: str, side_hustle: str):
    if apiKey != "1234567890": # checks if the API key is valid
        return { "error": "Invalid API Key" }
    elif side_hustle in side_hustles:
        return { "error": "Side hustle already exists" }
    elif len(side_hustle) < 1:
        return { "error": "Side hustle cannot be empty" }
    side_hustles.append(side_hustle) # adds new side hustle to the list
    return { "message": "Side hustle added successfully" }
    
@app.get("/money-quotes")
def get_money_quotes(QuoteRange: int, All: bool):
    if All:
        return { "money_quote": money_quotes }  # returns all money quotes
    if QuoteRange < 1:
        return { "error": "Invalid Quote Range" }
    return { "money_quote": random.sample(money_quotes, QuoteRange) }  # returns random money quotes based on range
    