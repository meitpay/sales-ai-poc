import { useState, useEffect, useRef, useCallback, Dispatch, SetStateAction } from 'react'
import { Alert, Button, Code, Group, Loader, SimpleGrid, Space } from '@mantine/core'
import AnsiToHtml from 'ansi-to-html'
import { IconInfoCircle } from '@tabler/icons-react'

const ansiToHtml: AnsiToHtml = new AnsiToHtml()

interface Props {
  data: Record<string, unknown>,
  url: string,
  loading: boolean,
  setLoading: Dispatch<SetStateAction<boolean>>
}

const StreamingComponent = ({ data, url, loading, setLoading }: Props) => {
  const [streamData, setStreamData] = useState('')
  const [error, setError] = useState<Record<string, boolean | string | undefined>>({ isError: false, message: undefined })
  const endOfStreamRef = useRef<HTMLDivElement>(null)
  const [reset, setReset] = useState(false)

  const scrollToEnd = useCallback(() => {
    if (endOfStreamRef.current) {
      endOfStreamRef.current.scrollIntoView({ behavior: 'smooth' })
    }
  }, [])

  useEffect(() => {
    const handler = setTimeout(() => {
      scrollToEnd()
    }, 100)

    return () => clearTimeout(handler)
  }, [streamData, scrollToEnd])

  useEffect(() => {
    let active = true
    const abortController = new AbortController()

    const fetchData = async () => {
      try {
        setReset(false)
        setLoading(true)
        setError({ isError: false, message: undefined })

        const response = await fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data),
          signal: abortController.signal
        })

        const reader = response?.body?.getReader()
        const decoder = new TextDecoder()

        const processResponse = async () => {
          const { done, value } = await (reader?.read() || { done: true })

          if (done) {
            if (active) {
              setLoading(false)
            }
            return
          }

          const decodedText = decoder.decode(value)
          const htmlText = ansiToHtml.toHtml(decodedText).replace(/\n/g, '<br/>')
          setStreamData(oldData => oldData + htmlText)

          await processResponse()
        }

        await processResponse()
      } catch (error) {
        if (active) {
          console.error('Fetch error:', error)
          const errorMessage = error instanceof Error ? error.message : 'Unable to fetch data'
          setError({ isError: true, message: errorMessage })
        }
      } finally {
        if (active) {
          console.log('finally')
          setLoading(false)
        }
      }
    }

    fetchData().then(() => console.log('fetching data'))

    return () => {
      active = false
      abortController.abort()
    }
  }, [data, setLoading, url])


  const handleReset = () => {
    setReset(true)
    setError({ isError: false, message: undefined })
    setLoading(false)
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
      {loading && <Loading />}

      {error.isError && <ErrorMessage />}
      <Space h='xs' />


      {!loading && (
        <SimpleGrid cols={2}>
          <Group>
            <h3>Task completed</h3>
          </Group>
          <Group justify='right'>
            <Button variant='light' color='red' onClick={handleReset}>Clear Data</Button>
          </Group>
        </SimpleGrid>)
      }

      <div ref={endOfStreamRef} />
      <Space h='xs' />

    </div>
  )
}

export default StreamingComponent
