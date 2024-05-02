import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import ErrorPage from './components/layout/error/ErrorPage.tsx'
import App from './App.tsx'
import { PersonSearch } from './components/form/PersonSearch.tsx'
import { MantineProvider } from '@mantine/core'
import { StrictMode } from 'react'
import Home from './components/home/Home.tsx'

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: '/',
        element: <Home />,
        index: true
      },
      {
        path: 'person-search',
        element: <PersonSearch />
      }
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <MantineProvider defaultColorScheme='dark'>
      <RouterProvider router={router} />
    </MantineProvider>
  </StrictMode>
)
