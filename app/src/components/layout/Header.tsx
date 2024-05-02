import { useState } from 'react'
import { Container, Group } from '@mantine/core'
import classes from './Header.module.css'
import { ThemeColor } from './AppTheme'
import { Link } from 'react-router-dom'

interface Links {
  link: string,
  label: string
}

const links: Links[] = [
  { link: '/', label: 'Home' },
  { link: '/job-listing', label: 'Job Listing' },
  { link: '/person-search', label: 'Person Search' }
]

export function Header() {
  const [active, setActive] = useState(links[0].link)

  const items = links.map((link: Links) => (
    <Link
      key={link.label}
      className={classes.link}
      data-active={active === link.link || undefined}
      onClick={() => {
        setActive(link.link)
      }}
      to={link.link}>
      {link.label}
    </Link>
  ))

  return (
    <header className={classes.header}>
      <Container size='xl' className={classes.inner}>
        <Group gap={5} visibleFrom='md'>
          {items}
        </Group>
        <ThemeColor />
      </Container>
    </header>
  )
}
