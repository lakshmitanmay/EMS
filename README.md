# Event Management System
My first project.

## **_Purpose?_**

I have noticed that there are a lot of comprehensive and all-in-one solutions for people who want to manage and organize their schedules, so that they don’t have to worry about what they have to do later. But these systems are for the general public, and the market is saturated.

But what about those who are on other side of things… the business side? Do they have any such type of systems to streamline their workflows and cater to their specific needs? The short answer is.. YES. But the long answer is… NO.

The general public only have very common needs that can be easily solved by a simple system. But here, it’s not so easy.

Take the people managing events for example. Sure, they can manage their events and their entire schedule on MS Excel or something, but it is not ideal. On top of that, specific solutions demand more money, which many people aren’t ready to pay for.

So, I took this specific niche: event management, and created an all-in-one solution for managing and organizing events safely and efficiently. The EMS I created may not compete with the big players, but it sure can be of help for those people and those companies, who are not able to pay huge amounts for such comprehensive systems.

## **_So.. How does it actually work?_**

The EMS is actually very simple. I used basic Python and MySQL connectivity to create this EMS.

The EMS features USER LOGIN capability, so that you each user can store their respectively events separately and securely with their own username and password.

The welcome screen features REGISTRATION and USER LOGIN functions.

After logging in, the Dashboard screen features:

1.   Event Management

2.   Logistics Management

3.   Attendee Management

The 3 crucial parts of organizing any event successfully.

Each section has further sub sections that allow you to do various tasks like displaying, searching, updating and deleting.

At its core, all the data is stored in a unified database in MySQL, ensuring quick and easy access to the data with, or without the use of this Python based interface of this EMS.

Using the EMS is simple. The interface makes sure you are in the right place every step of the way and allows you to move forward and backward in the interface.

A single event is denoted by its own unique Event ID, which ensures that there is no chance of redundancy for about 100000 events.

## ***Objectives***
My project has 5 basic objectives.

**_1. Streamlined Event Creation and Management:_**

- Enable users to create, organize, and manage events efficiently through a user-friendly interface.
- Provide functionalities for defining event details, including names, dates, venues, descriptions, and associated resources.

**_2. Efficient Attendee Management:_**

- Facilitate attendee registration, tracking, and engagement for various event types.
- Offer a seamless registration process and attendee communication channels for enhanced user experience.

**_3. Robust Resource and Logistics Management:_**

- Manage venues, equipment, staff allocation, transportation, and inventory effectively.
- Optimize resource utilization, track logistics, and ensure smooth operations for events of diverse scales.

**_4. Secure User Authentication and Authorization:_**

- Implement robust authentication mechanisms to ensure secure access to the system.
- Define and enforce role-based access control to safeguard sensitive data and functionalities.

**_5. Cost Effective; made for small businesses and event organisers:_**

- Optimize resource allocation and automate manual processes to reduce costs and save time.
- Minimize administrative overheads and improve operational efficiency to maximize resource utilization.

## ***Modules Used***
1. Random Module
2. MySQL.connector module


## **_Limitations_**:

1. Not made for large businesses

2. Limited Number of events are possible to be stored

3. Password functionality isn’t very secure; it has no encryption.

4. Limited number of things can be stored regarding each event.

5. UX is good but pretty subpar UI.

## **_Future scope:_**

1. Adaptable for large businesses

2. Unlimited number of events can be stored.

3. Adding encryption to passwords.

4. Ability to change and add what things can be stored regarding each event.

5. Make the Python based interface more focused on UI.
## **_Conclusion_**

In the end, all I would like to say is.. This is not anything revolutionary. But what I have created is a cost-effective way for small business and event organizers to manage their events easily and securely. Even the most non-tech savvy user will also be able to manage any type of event with ease using this EMS.