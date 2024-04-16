import { useState, useEffect, useRef } from 'react'
import { Alert, Button, Code, Group, Loader, Space } from '@mantine/core'
import AnsiToHtml from 'ansi-to-html'
import { IconInfoCircle } from '@tabler/icons-react'

const ansiToHtml = new AnsiToHtml()

interface Props {
  data: Record<string, unknown>,
  url: string
}

const StreamingComponent = ({ data, url }: Props) => {
  const [streamData, setStreamData] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<Record<string, boolean | string | undefined>>({ isError: false, message: undefined })
  const endOfStreamRef = useRef<HTMLDivElement>(null)
  const [reset, setReset] = useState(false)

  useEffect(() => {
    endOfStreamRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [streamData])

  useEffect(() => {
    const fetchData = async () => {
      setReset(false)
      setIsLoading(true)
      setError({ isError: false, message: undefined })
      try {
        const response = await fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        })

        const reader = response?.body?.getReader()
        const decoder = new TextDecoder()

        return reader?.read().then(async function processText({ done, value }): Promise<void> {
          if (done) {
            setIsLoading(false)
            return
          }

          const decodedText = decoder.decode(value)
          const htmlText = ansiToHtml.toHtml(decodedText).replace(/\n/g, '<br/>')
          setStreamData(oldData => oldData + htmlText)
          return await processText(await reader.read())
        })

      } catch (error: Error | unknown) {
        console.error('Fetch error:', error)
        setError({ isError: true, message: error instanceof Error ? error.message : 'Unable to fetch data' })
        setIsLoading(false)
      }
    }

    fetchData().then(() => console.log('done'))
  }, [data, url])

  const handleReset = () => {
    setReset(true)
    setError({ isError: false, message: undefined })
    setIsLoading(false)
    setStreamData('')
  }

  const ErrorMessage = () => {
    return (
      <Alert variant='light' color='blue' title='Unable to create report' icon={<IconInfoCircle />}>
        {error?.message ?? 'Something wrong happened. If this error persists, please contact support.'}
      </Alert>
    )
  }

  const Loading = () => {
    return (
      <Group justify='center'>
        <Loader color='teal' type='dots' />
      </Group>
    )
  }

  if (reset) {
    return <></>
  }

  return (
    <div>
      <h1>Response</h1>
      <Code block dangerouslySetInnerHTML={{ __html: streamData }} style={{ whiteSpace: 'pre-wrap' }} />
      {isLoading && <Loading />}

      {error.isError && <ErrorMessage />}
      <Space h='xs' />

      <Group justify='right'>
        <Button variant='light' color='red' onClick={handleReset}>Clear Data</Button>
      </Group>
      <div ref={endOfStreamRef} />
      <Space h='xs' />

    </div>
  )
}

export default StreamingComponent
