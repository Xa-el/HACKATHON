import React from 'react';
import ReactDOM from 'react-dom/client';
<<<<<<< Updated upstream
//import LoginPage from './Login';
import SignUpPage from "./Signup.jsx";
//import SignUpPage from './Signup';
//import CustomProfile from './Profile';
import Chat from './Chat'; // Adjust the path according to your file structure


=======
import LoginPage from './Login';
import SignUpPage from './Signup';
import CustomProfile from './Profile';
// import { UserProvider } from './UserContext';
import DMs from './directmessage';
import Homepage from './homepage';
>>>>>>> Stashed changes

// Assuming your public/index.html file has a div with id='root'
const rootElement = document.getElementById('root');
const root = ReactDOM.createRoot(rootElement);

root.render(
<<<<<<< Updated upstream
    <React.StrictMode>
        {/* <SignUpPage /> */}
        <Chat />
    </React.StrictMode>);
=======
  <React.StrictMode>
    <DMs />
  </React.StrictMode>);
>>>>>>> Stashed changes
