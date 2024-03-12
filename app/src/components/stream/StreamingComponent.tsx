import { useState, useEffect } from 'react'
import { Code } from '@mantine/core'

const API_ENDPOINT = import.meta.env.VITE_API_URL ?? 'http://localhost:5000'

interface Props {
  data: {
    domain: string,
    company: string,
    needs: string,
    benefits: string
  }
}

const StreamingComponent = ({ data }: Props) => {
  const [streamData, setStreamData] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true)
      try {
        const response = await fetch(`${API_ENDPOINT}/process-data`, {
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
        setIsLoading(false)
      }
    }

    fetchData().then(() => console.log('All done'))
  }, [data])

  return (
    <div>
      <h3>Streamed Data:</h3>
      {isLoading && <p>Fetching data...</p>}
      <Code block dangerouslySetInnerHTML={{ __html: streamData }} style={{ whiteSpace: 'pre-wrap' }} />
    </div>
  )
}

export default StreamingComponent
