import { useState, useEffect } from 'react'
import { Code } from '@mantine/core'

interface Props {
  data: Record<string, unknown>,
  url: string
}

const StreamingComponent = ({ data, url }: Props) => {
  const [streamData, setStreamData] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [isError, setIsError] = useState(false)

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true)
      setIsError(false)
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

          setStreamData(oldData => oldData + decoder.decode(value).replace(/\n/g, '<br/>'))
          return await processText(await reader.read())
        })

      } catch (error) {
        console.error('Fetch error:', error)
        setIsError(true)
        setIsLoading(false)
      }
    }

    fetchData().then(() => setIsLoading(false))
  }, [data, url])

  return (
    <div>
      <h3>Response</h3>
      {isLoading && <p>Working...</p>}
      {isError && <p>Something wrong happened...</p>}
      <Code block dangerouslySetInnerHTML={{ __html: streamData }} style={{ whiteSpace: 'pre-wrap' }} />
    </div>
  )
}

export default StreamingComponent
