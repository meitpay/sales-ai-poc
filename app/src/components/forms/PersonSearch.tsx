import { Box, Button, Group, TextInput, Textarea, Container, Space, Divider, Text } from '@mantine/core'
import { useForm } from '@mantine/form'
import { useState } from 'react'
import StreamingComponent from '../stream/StreamingComponent.tsx'
import { isStringLengthZero } from '../../utils/stringUtils.ts'

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
      person: (value) => isStringLengthZero(value) ? 'Missing name of the person' : null,
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
          <TextInput label={fields.person.label}
                     placeholder={fields.person.description} {...form.getInputProps('person')} />

          <Textarea autosize label={fields.miscInfo.label}
                    placeholder={fields.miscInfo.description} {...form.getInputProps('miscInfo')} />

          <Divider my='md' />

          <Text fw={500}>
            {fields.websites.label}
          </Text>

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

          <Space h='xs' />

          <Group grow>
            <Button onClick={() => addField('websites')}>Add Website</Button>
            <Button color='red' onClick={() => removeField('websites', form.values.websites.length)}>Remove Website</Button>
          </Group>

          <Divider my='md' />

          <Text fw={500}>
            {fields.soMeProfiles.label}
          </Text>

          {form.values.soMeProfiles.map((_, index) => (
            <Group key={index}>
              <TextInput
                style={{ width: '100%' }}
                placeholder={fields.soMeProfiles.description}
                {...form.getInputProps(`soMeProfiles.${index}`)}
              />
            </Group>
          ))}

          <Space h='xs' />

          <Group grow>
            <Button onClick={() => addField('soMeProfiles')}>Add Social Media Profile</Button>
            <Button color='red' onClick={() => removeField('soMeProfiles', form.values.soMeProfiles.length)}>Remove Social Media Profile</Button>
          </Group>

          <Divider my='md' />
          <Group grow>
            <Button type='submit' mt='md'>
              Submit
            </Button>
            <Button color='red' type='reset' mt='md' onClick={() => {
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
