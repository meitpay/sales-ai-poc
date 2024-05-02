import { useRouteError } from 'react-router-dom'
import { Header } from '../header/Header.tsx'
import { Container } from '@mantine/core'

interface RouteError {
  statusText?: string;
  message?: string;
}

export default function ErrorPage() {
  const error = useRouteError() as RouteError | null
  console.error(error)

  return (
    <>
      <Header />
      <Container>

        <h1>Oops!</h1>
        <p>Sorry, an unexpected error has occurred.</p>
        <p>
          <i>{error?.statusText || error?.message || 'Unknown error'}</i>
        </p>
      </Container>
    </>
  )
}
