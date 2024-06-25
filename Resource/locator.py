import  datetime
from datetime import timedelta

current_datetime = datetime.datetime.now()
current_date = current_datetime.date()
two_days = datetime.timedelta(days=2)
three_days = datetime.timedelta(days=3)
rent_date = current_date + two_days
start_date = rent_date.strftime("%d")
future_date = current_date + three_days
end_date = future_date.strftime("%d")

carRent = "//div[@id='__next']/div[4]/div[2]/div/div[2]/div/div/div/div/div[6]/div"
rentalLocation = "//div[@id='__next']/div[4]/div[2]/div/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/input"
rentalDate = "//div[@id='__next']/div[4]/div[2]/div/div[2]/div/div[3]/div/div/div/div/div[2]/div/div[3]/div/div/div/input"
jakartaBarat = "//div[@id='__next']/div[4]/div[2]/div/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[3]"
rentDate = "//input[@data-testid='rental-search-form-date-input-start']"
rentTime = "//input[@data-testid='rental-search-form-time-input-start']"
pickDate = f"(//div[@dir='auto'][normalize-space()='{start_date}'])[1]"
rentEndDate = "//input[@data-testid='rental-search-form-date-input-end']"
endDate = f"(//div[@dir='auto'][normalize-space()='{end_date}'])[5]"
searchCar = "(//div[@class='css-901oao r-1awozwy r-jwli3a r-6koalj r-61z16t'])[1]"
selectCar = "(//div[@dir='auto'][normalize-space()='Continue'])[2]"
selectCarProvider = "(//div[@dir='auto'][normalize-space()='Continue'])[2]"
pickupRentalOffice = "(//div[@class='css-901oao r-t1w4ow r-ubezar r-majxgm r-135wba7 r-fdjqy7'][normalize-space()='Rental Office'])[1]"
pickupLocation = "(//div[@class='css-901oao css-bfa6kz r-13awgt0 r-t1w4ow r-ubezar r-majxgm r-135wba7 r-1m04atk r-fdjqy7'])[1]"
selectPickup = "(//div[@class='css-1dbjc4n r-1loqt21 r-1otgn73 r-1i6wzkk r-lrvibr r-13qz1uu'])[1]"
dropOffOther = "(//div[@class='css-901oao r-t1w4ow r-ubezar r-majxgm r-135wba7 r-fdjqy7'][normalize-space()='Other Locations'])[2]"
dropOffAddress = "(//input[@placeholder='Search location or address'])[2]"
selectDropOff = "(//div[@aria-label='South Jakarta'])[1]"
continueBook = "(//div[@class='css-901oao css-bfa6kz r-jwli3a r-t1w4ow r-cygvgh r-b88u0q r-1iukymi r-q4m81j'][normalize-space()='Continue'])[1]"
contactFullName = "(//input[@type='text'])[1]"
contactPhoneNumber = "(//input[@aria-label='Phone Number'])[1]"
contactEmail = "(//input[@aria-labelledby='emailAddress'])[1]"
driverTitle = "(//select[@class='r-30o5oe r-1niwhzg r-1yadl64 r-1p0dtai r-t1w4ow r-ubezar r-majxgm r-1pi2tsx r-1r74h94 r-135wba7 r-crgep1 r-orgf3d r-1ny4l3l r-10paoce r-u8s1d r-3mc0re r-ipm5af r-34rx7k r-417010'])[1]"
driverFullName = "(//input[@type='text'])[3]"
driverPhoneNumber = "(//input[@aria-label='Phone Number'])[2]"
submitBooking = "(//div[@class='css-901oao css-bfa6kz r-jwli3a r-t1w4ow r-cygvgh r-b88u0q r-1iukymi r-q4m81j'])[1]"
rentalRequirements = "(//div[@class='css-1dbjc4n r-13awgt0 r-18u37iz'])[1]"
checkAll = "(//div[@class='css-1dbjc4n r-1awozwy r-18u37iz r-633pao'])[1]"
saveRequirements = "(//div[@role='button'])[8]"
continuePayment = "(//div[@class='css-901oao css-bfa6kz r-jwli3a r-t1w4ow r-1uirtdp r-b88u0q r-uzxld0 r-q4m81j'])[1]"
confirmBooking = "(//div[@class='css-901oao css-bfa6kz r-jwli3a r-t1w4ow r-cygvgh r-b88u0q r-1iukymi r-q4m81j'])[1]"
mandiriVa = "(//div[@class='css-1dbjc4n r-1fuqb1j r-d045u9 r-1472mwg r-u8s1d r-lrsllp'])[3]"
confirmPayment = "(//div[@class='css-901oao css-bfa6kz r-t1w4ow r-1uirtdp r-b88u0q r-uzxld0 r-q4m81j'])[1]"
passengerList = "(//div[@class='css-901oao r-1ihkh82 r-t1w4ow r-1b43r93 r-majxgm r-rjixqe r-ymttw5 r-5njf8e r-fdjqy7'])[1]"