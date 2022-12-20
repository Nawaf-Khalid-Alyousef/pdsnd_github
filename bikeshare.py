#Worrrrrrrrkkkkrkrkrk
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    thecities = ('Chicago', 'New York City', 'Washington')
    while True:
      city = input("\nWhich city do you wish to look through? Chicago, New York City, and Washington.\n")
      if city not in thecities:
        print("Sincerely apologize for missing it. Feel free to try again.")
        continue      
      elif city in thecities:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    themonths = ('all','January', 'February', 'March', 'April', 'May', 'June')
    while True:
      month = input("\nWhich month do you wish to look through? (all, January, February, ... , June)\n")
      if month not in themonths:
        print("Sincerely apologize for missing it. Feel free to try again.")
        continue      
      elif month in themonths:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    thedays = ('all', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday')
    while True:
      day = input("\nWhich day of week do you wish to look through? (all, Monday, Tuesday, ... Sunday)\n") 
      if day not in thedays:
        print("Sincerely apologize for missing it. Feel free to try again.")
        continue      
      elif day in thedays:
        break

    print('-'*40)
    return city, month, day       
#########################################################################################################     
###        ////Reference : https://stackoverflow.com/questions/53086118/python-for-dummies-using-the-bakeshare-data
 #########################################################################################################

def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

#########################################################################################################
## /// Referance: https://classroom.udacity.com/nanodegrees/nd104-mcit/parts/cd0024/modules/bb139072-8b52-4e4b-90d5-e08be527a353/lessons/ls1727/concepts/7a33cce4-18de-48a4-8aeb-d0c13c972909
#########################################################################################################

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].value_counts().idxmax()
    print("the most common month:",common_month)

    # TO DO: display the most common day of week
    common_day_of_week=df['day_of_week'].value_counts().idxmax()
    print("the most common day of week:",common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour  ###//https://www.geeksforgeeks.org/python-pandas-series-dt-hour/
    common_start_hour=df['hour'].value_counts().idxmax()
    print("the most common start hour:",common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#########################################################################################################
 ##   /// Referance: https://datascienceparichay.com/article/most-frequent-value-in-a-pandas-column/
 #########################################################################################################

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station=df['Start Station'].value_counts().idxmax()
    print("the most common start station:",commonly_start_station)

    # TO DO: display most commonly used end station
    commonly_end_station=df['End Station'].value_counts().idxmax()
    print("the most common end station:",commonly_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination=df.groupby(['Start Station','End Station']).size().idxmax()
    print("the most common frequent combination of start station and end station trip:",most_frequent_combination)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
#########################################################################################################
## /// Referance: https://datascienceparichay.com/article/most-frequent-value-in-a-pandas-column/
## /// Referance: https://stackoverflow.com/questions/53037698/how-can-i-find-the-most-frequent-two-column-combination-in-a-dataframe-in-python
#########################################################################################################



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time:",df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print("mean travel time:",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types:",df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print("counts of gender:",df['Gender'].value_counts())
    except KeyError:
           print("Something else went wrong")

    # TO DO: Display earliest, most recent, and most common year of birth
    try: 
      print("Most Earliest Year Of Birth:",df['Birth Year'].min())
    except KeyError:
      print("Something else went wrong")

    try: 
      print("Most Recent Year Of Birth:",df['Birth Year'].max())
    except KeyError:
      print("Something else went wrong") 
    try: 
      print("Most Common Year Of Birth:",df['Birth Year'].value_counts().idxmax())
    except KeyError:
      print("Something else went wrong")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#########################################################################################################
# /// Referance: https://www.codingem.com/try-catch-in-python/
# /// Referance: https://realpython.com/python-keyerror/
#########################################################################################################

def display_data(df):
   view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
   start_loc = 0
   End_loc = 5
   while view_data == 'yes':
      print(df.iloc[start_loc:End_loc])
      start_loc += 5
      End_loc += 5
      view_data = input("Do you wish to continue?: ").lower()
      
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        display_data(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()