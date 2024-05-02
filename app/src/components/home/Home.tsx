import { Container, Title } from '@mantine/core'
import { Link } from 'react-router-dom'

const Home = () => {
  return (
    <Container>
      <Title order={3} size='h1'>
        Sales AI
      </Title>
      <p>
        This application is using AI Agents to create reports on persons and companies.
      </p>
      <p>
        Head over to <Link to={'/person-search'}>person search</Link> our navigate with the top navbar to create a report on a person.
      </p>
    </Container>
  )
}

export default Home
