import { Box, Button, Code, Group, TextInput, Textarea } from '@mantine/core'
import { useForm } from '@mantine/form'
import { useState } from 'react'
import { isStringLengthZero, isValidURL, prependHttpsToURL } from '../../utils/stringUtils'

const SalesForm = () => {
  const [submittedValues, setSubmittedValues] = useState('')

  const form = useForm({
    initialValues: {
      domain: '',
      company: '',
      needs: '',
      benefits: ''
    },
    validate: {
      domain: (value) => !isValidURL(value) ? 'Missing or invalid URL' : null,
      company: (value) => isStringLengthZero(value) ? 'Missing description' : null,
      needs: (value) => isStringLengthZero(value) ? 'Missing hiring needs' : null,
      benefits: (value) => isStringLengthZero(value) ? 'Missing benefits' : null
    }
  })


  const fields = {
    domain: {
      label: 'What is the company domain',
      description: 'https://itera.com'
    },
    company: {
      label: 'What is the company description',
      description: 'Itera is a tech company that is a specialist in sustainable digital transformation'
    },
    needs: {
      label: 'What are the hiring needs',
      description: 'Software/Data/AI/Analytics/Cloud engineers and scientists'
    },
    benefits: {
      label: 'Company What are specific_benefits you offer',
      description: 'Hybrid work location, great work environment, self development and more!'
    }
  }

  return (
    <Box maw={720} mx="auto">
      <form onSubmit={form.onSubmit((values) => {
        values.domain = prependHttpsToURL(values.domain)
        setSubmittedValues(JSON.stringify(values, null, 2))
      })}>
        <TextInput label={fields.domain.label}
                   placeholder={fields.domain.description} {...form.getInputProps('domain')} />
        <Textarea autosize label={fields.company.label}
                  placeholder={fields.company.description} {...form.getInputProps('company')} />
        <Textarea autosize label={fields.needs.label}
                  placeholder={fields.needs.description} {...form.getInputProps('needs')} />
        <Textarea autosize label={fields.benefits.label}
                  placeholder={fields.benefits.description} {...form.getInputProps('benefits')} />

        <Group>
          <Button type="submit" mt="md">
            Submit
          </Button>
          <Button color="red" type="reset" mt="md" onClick={() => {
            form.reset()
            setSubmittedValues('')
          }}>
            Reset to initial values
          </Button>
        </Group>

        {submittedValues && <Code block style={{ marginTop: '10px' }}>{submittedValues}</Code>}
      </form>

    </Box>
  )
}

export {
  SalesForm
}
