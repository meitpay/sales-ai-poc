import { useState } from 'react'
import { Container, Group } from '@mantine/core'
import classes from './Header.module.css'
import { ThemeColor } from './AppTheme'

const links = [
  { link: '/', label: 'Home' },
  { link: '/faq', label: 'FAQ' }
]

export function Header() {
  const [active, setActive] = useState(links[0].link)

  const items = links.map((link) => (
    <a
      key={link.label}
      href={link.link}
      className={classes.link}
      data-active={active === link.link || undefined}
      onClick={(event) => {
        event.preventDefault()
        setActive(link.link)
      }}
    >
      {link.label}
    </a>
  ))

  return (
    <header className={classes.header}>
      <Container size="xl" className={classes.inner}>
        <Group gap={5} visibleFrom="md">
          {items}
        </Group>
        <ThemeColor />
      </Container>
    </header>
  )
}
