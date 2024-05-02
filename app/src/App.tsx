import '@mantine/core/styles.css'
import { Header } from './components/layout/header/Header.tsx'
import { Outlet } from 'react-router-dom'

function App() {
  return (
    <>
      <Header />
      <Outlet />
    </>
  )
}

export default App
