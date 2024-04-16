import { Box, Button, Group, TextInput, Textarea, Container, Space, Divider, Text, Grid } from '@mantine/core'
import { useForm } from '@mantine/form'
import { useState } from 'react'
import StreamingComponent from '../stream/StreamingComponent.tsx'
import { isStringLengthZero } from '../../utils/stringUtils.ts'
import { IconMinus, IconPlus } from '@tabler/icons-react'

const API_ENDPOINT = import.meta.env.VITE_API_URL ?? 'http://localhost:5000'

const PersonSearch = () => {

  const form = useForm({
    initialValues: {
      person: '',
      websites: [],
      miscInfo: '',
      soMeProfiles: []
    },
    validate: {
      person: (value: string): string | null => isStringLengthZero(value) ? 'Missing name of the person' : null
    }
  })

  const [submittedValues, setSubmittedValues] = useState<Record<string, unknown> | undefined>(undefined)

  const addField = (fieldName: string) => {
    form.insertListItem(fieldName, '')
  }

  const removeField = (fieldName: string, index: number) => {
    form.removeListItem(fieldName, index - 1)
  }

  const fields = {
    person: {
      label: 'Name of the person',
      description: 'John Smith'
    },
    websites: {
      label: 'Website to search. e.g. Company website, news site, etc',
      description: 'https://itera.com'
    },
    miscInfo: {
      label: 'Do you have any additional information about the person?',
      description: 'Lives in X City, Y years old, from Z town etc'
    },
    soMeProfiles: {
      label: 'Social media accounts e.g. LinkedIn, Twitter, etc',
      description: 'https://twitter.com/elonmusk'
    }
  }

  return (
    <Container>
      <Box mx='auto'>
        <form onSubmit={form.onSubmit((values) => {
          setSubmittedValues(values)
        })}>
          <TextInput label={fields.person.label} placeholder={fields.person.description} {...form.getInputProps('person')} />

          <Textarea autosize label={fields.miscInfo.label} placeholder={fields.miscInfo.description} {...form.getInputProps('miscInfo')} />

          <Divider my='md' />

          <Grid>
            <Grid.Col span={10}>
              <Text fw={500}>
                {fields.websites.label}
              </Text>
            </Grid.Col>
            <Grid.Col span={1}>
              <Button variant='light' color={'teal'} onClick={() => addField('websites')}><IconPlus /></Button>
            </Grid.Col>
            <Grid.Col span={1}>
              <Button variant='light' color='red' onClick={() => removeField('websites', form.values.websites.length)}><IconMinus /></Button>
            </Grid.Col>
          </Grid>

          {form.values.websites.map((_, index) => (
            <Group key={index}>
              <Space h='xs' />
              <TextInput
                style={{ width: '100%' }}
                placeholder={fields.websites.description}
                {...form.getInputProps(`websites.${index}`)}
              />
            </Group>
          ))}

          <Divider my='md' />

          <Grid>
            <Grid.Col span={10}>
              <Text fw={500}>
                {fields.soMeProfiles.label}
              </Text>
            </Grid.Col>
            <Grid.Col span={1}>
              <Button variant='light' color={'teal'} onClick={() => addField('soMeProfiles')}><IconPlus /></Button>
            </Grid.Col>
            <Grid.Col span={1}>
              <Button variant='light' color='red' onClick={() => removeField('soMeProfiles', form.values.soMeProfiles.length)}><IconMinus /></Button>
            </Grid.Col>
          </Grid>

          {form.values.soMeProfiles.map((_, index) => (
            <Group key={index}>
              <Space h='xs' />

              <TextInput
                style={{ width: '100%' }}
                placeholder={fields.soMeProfiles.description}
                {...form.getInputProps(`soMeProfiles.${index}`)}
              />
            </Group>
          ))}

          <Divider my='md' />
          <Group grow>
            <Button variant='light' color='teal' type='submit' mt='md'>
              Submit
            </Button>
            <Button variant='light' color='red' type='reset' mt='md' onClick={() => {
              form.reset()
              setSubmittedValues(undefined)
            }}>
              Reset to initial values
            </Button>
          </Group>
        </form>
      </Box>

      {submittedValues && <StreamingComponent data={submittedValues} url={`${API_ENDPOINT}/person-search`} />}

    </Container>
  )
}

export {
  PersonSearch
}
