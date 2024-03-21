import '@mantine/core/styles.css'
import { Header } from './components/layout/Header'
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
