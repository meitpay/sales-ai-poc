import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import ErrorPage from './components/layout/ErrorPage.tsx'
import App from './App.tsx'
import { JobListing } from './components/forms/JobListing.tsx'
import { PeopleSearch } from './components/forms/PeopleSearch.tsx'
import { MantineProvider } from '@mantine/core'

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: 'job-listing',
        element: <JobListing />
      },
      {
        path: 'people-search',
        element: <PeopleSearch />
      }
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <MantineProvider defaultColorScheme='dark'>
      <RouterProvider router={router} />
    </MantineProvider>
  </React.StrictMode>
)
