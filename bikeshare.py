import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv','chicago city': 'chicago.csv',
              'newyork': 'new_york_city.csv', 'new york': 'new_york_city.csv', 'new york city': 'new_york_city.csv', 
              'washington': 'washington.csv' , 'washington city ': 'washington.csv'}
day_switch ={
        'monday': 0,'mon': 0,
        'tuesday': 1,'tue': 1,
        'wednesday': 2,'wed': 2,
        'thursday': 3,'thu': 3,
        'friday': 4,'fri': 4,
        'saturday': 5,'sat': 5,
        'sunday': 6,'sun': 6,
        'all': 9,
    }

month_switch ={
        'all':'0',
         '1':'01',
         '2':'02',
         '3':'03',
         '4':'04',
         '5':'05',
         '6':'06',
         '7':'07',
         '8':'08',
         '9':'09',
         '10':'10',
         '11':'11',
         '12':'12',
    }



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n\nHello! /ln Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs 
    while True :
        try:
            city = (input('\n \n can you please enter the city name ? EX: chicago, newyork , washington .    ')).lower()
            if city in CITY_DATA.keys():
                break
            else:
                print(' Enter the city name correctly!!! ')
        except:
            print("Try again!!!")

    # set default value 
    month = 'all'
    day = 'all' 
    
    filter_type = (input('Do you want to apply any filter on your data ? month or day or both ? ')).lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    
    while ((filter_type == 'month' ) or (filter_type == 'both' )) :
        try:
            month = (input('Enter the number of month . EX: 1,2,3,...,12,all.  ')).lower()
            if ( (month <= 'all ' )or (int(month) < 13 and int(month) > 0)  ):
                break
            else:
                print('Please enter month number between 1 to 12 or all :)')    
        except:
            print("Try again!!!")

    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while ((filter_type == 'both' ) or (filter_type == 'day' ))  :
        try:
            day = (input('Enter the name of the day . EX: sunday,mon,all.  ')).lower()
            if day in day_switch.keys():
                break
            else:
                print(' Enter the day name correctly !!! ')
        except:
            print("Try again!!!")


    print('-'*40)
    

    return city, month_switch[month] , day_switch[day]


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
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['day_number_of_ST']= df['Start Time'].dt.dayofweek # add day number column in the dataframe  

    # cheak day value , if it 9 the do not apply filter by day 
    if day!=9:
       df = df[df['day_number_of_ST'] == day]


    # cheak month value , if it 0 the do not apply filter by month 
    if month != '0' :
       df = df[df['Start Time'].dt.strftime('%m') == month]  


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    most_month = df['Start Time'].dt.strftime('%m'). value_counts(). idxmax()
    print(df.head())
    print(f'\nThe most common month is  { most_month }') 
    
    # TO DO: display the most common day of week

    most_day = df['day_number_of_ST']. value_counts(). idxmax()
    print('\nThe most common day is  ',{list(day_switch.keys())
      [list(day_switch.values()).index(most_day)] })

    

    # TO DO: display the most common start hour

    most_hour = df['Start Time'].dt.strftime('%I'). value_counts(). idxmax()
    print(f'\nThe most common hour is  { most_hour}' ) 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    most_start_st = df['Start Station']. value_counts(). idxmax()
    print(f'\nThe most common Start Station is { most_start_st}' ) 
    

    # TO DO: display most commonly used end station
    
    most_start_et = df['End Station']. value_counts(). idxmax()
    print(f'\nThe most common End Station is { most_start_et}' ) 
    

    # TO DO: display most frequent combination of start station and end station trip

    print('\nThe most common combination station is ',  df.groupby(['Start Station','End Station']).size().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print('\nThe total travel timeis  ',df['Trip Duration'].count() ) 


    # TO DO: display mean travel time

    print('\nThe average travel timeis  ' ,df['Trip Duration'].mean() )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        df2=df.groupby(['User Type'])['Trip Duration'].count()
        index = df2.index

        j=0
        for i in index:
           print(f'{i}:   {df2[j]}')
           j += 1

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        df3=df.groupby(['Gender'])['Trip Duration'].count()
        index2 = df3.index

        j=0
        for i in index2:
            print(f'{i}:   {df3[j]}')
            j += 1

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        print('\nthe earliest year of birth, ',int(df['Birth Year'].min()),'\nthe most recent year, ',
         int(df['Birth Year'].max()),' \nand most common year of birth' , int(df['Birth Year'].value_counts().idxmax()) )




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if  not df.empty :
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)


            see_rowD = input('\nWould you like to view 5 rows of individual trip data? \n').lower()
            i=0
            while see_rowD != 'no':
               print(df.loc[i:(i+5),:])
               i += 5 
               see_rowD = input('\nWould you like to continue ? \n').lower()



        else:
            print(' thera is no record for your spcific filtter')

        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
