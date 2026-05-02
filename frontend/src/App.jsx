import { useState } from 'react'
import './App.css'
import RegisterPage from './RegisterPage'
import LoginPage from './LoginPage';
import JobListingPage from './JobListingPage';
import ApplyJobPage from './ApplyJobPage';
import { BrowserRouter, Route, Routes } from 'react-router-dom'


function App() {

  return (
    <BrowserRouter>
        <Routes>
          <Route path='/register' element={<RegisterPage/>}/>
          <Route path='/login' element={<LoginPage/>}/>
          <Route path='/jobs' element={<JobListingPage/>}/>
          <Route path='/apply/:jobId' element={<ApplyJobPage/>}/>
          
        </Routes>

    </BrowserRouter>
  )
}

export default App
