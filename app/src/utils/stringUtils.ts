/**
 * Checks if the given URL is valid.
 * @param {string} url - The URL to be validated.
 * @returns {boolean} - True if the URL is valid, false otherwise.
 */
const isValidURL = (url: string): boolean => {
  // Check if the URL is not empty
  if (isStringLengthZero(url)) {
    return false
  }

  // Prepend 'https://' to the URL if not present
  url = prependHttpsToURL(url)

  // Define the pattern for a valid URL using regular expression
  const pattern = new RegExp(
    '^(https?:\\/\\/)?' + // protocol
    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|' + // domain name
    '((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
    '(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
    '(\\#[-a-z\\d_]*)?$', // fragment locator
    'i'
  )

  // Test the URL against the defined pattern and return the result
  return pattern.test(url)
}

/**
 * Prepends 'https://' to the given URL if it doesn't already have a protocol.
 *
 * @param {string} url - The URL to prepend 'https://' to.
 * @return {string} The URL with 'https://' prepended if necessary.
 */
const prependHttpsToURL = (url: string): string => {
  url = decodeURIComponent(url)
  if (!/^(?:f|ht)tps?:\/\//.test(url)) {
    url = 'https://' + url
  }
  return url
}

/**
 * Check if the length of the input string after removing leading and trailing whitespace is zero.
 *
 * @param {string} input - The input string to check
 * @return {boolean} true if the length of the input string after removing leading and trailing whitespace is zero, false otherwise
 */
const isStringLengthZero = (input: string): boolean => {
  return input.trim().length === 0
}

export {
  isValidURL,
  isStringLengthZero,
  prependHttpsToURL
}
