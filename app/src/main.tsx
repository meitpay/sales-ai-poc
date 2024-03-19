import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import ErrorPage from './components/layout/ErrorPage.tsx'
import App from './App.tsx'
import { JobListing } from './components/forms/JobListing.tsx'
import { PersonSearch } from './components/forms/PersonSearch.tsx'
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
        element: <PersonSearch />
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
