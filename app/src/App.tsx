import '@mantine/core/styles.css'
import { MantineProvider } from '@mantine/core'
import { SalesForm } from './components/forms/SalesForm'
import { Header } from './components/layout/Header'

function App() {
  return (
    <MantineProvider defaultColorScheme="dark">
      <Header />
      <SalesForm />
    </MantineProvider>
  )
}

export default App
