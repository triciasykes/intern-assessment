Use the figma files
<a target="_blank" href="https://www.figma.com/files/project/60851741/Frontend-Dev-Challenge?fuid=1090284691689012784" rel="noreferrer">HERE</a>
and do the best you can to match the features you create to those designs.

- Part 1: Complete the navbar</h5>
    - Add the icon to the far right of the navigation bar that shows the user’s initial. There is a user object in the applications state (App.js) where you can pull their first initial from.
    - Make the navigation links (Home, Contacts) dynamic. The link for the page you are currently on should be black and bold, while the other links remain gray.
    - Make the navigation links work. Currently they aren’t active. They should allow us to navigate between the two pages!
    
    
    <h5 className="section-title">Part 2: Complete the contacts page</h5>
    <p>
        On the contacts component, we want to show a list of clients so our coach can easily see and get in touch with them. For the purposes of the challenge, you can use <a href="https://random-data-api.com/documentation" target="_blank" className='api-link' rel="noreferrer">THIS</a> random user generator api to get a list of fake clients. In the documentation you'll see an endpoint for "Users". This is the one you should use!
    </p>
    <ol>
        <li>Using fetch or the HTTP client of your choosing, retrieve a list of 20 users from the API and use a state variable to store them in the ‘Contacts’ component.</li>
        <li>Display the list of contacts as you see them in the ‘Contacts’ Figma design. The card should show the contact’s first name, last name, email address, and image.</li>
        <li>Add a hover effect to the contact cards. See the Figma board for this design!</li>
    </ol>
