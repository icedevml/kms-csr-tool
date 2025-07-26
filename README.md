# Google Cloud KMS - CSR generation tool

> [!CAUTION]
> This project is archived and is not maintained anymore.
> Please see [icedevml/pykmstool](https://github.com/icedevml/pykmstool) for a modernized and maintained version of this tool.

This tool could help you to generate a Certificate Signing Request (CSR) using a key that was generated inside a HSM provided by Google Cloud KMS. Especially, such CSRs might be demanded by a Certificate Authority in order to issue a certificate.

## No warranty on the tool

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Usage

1. Run the following command:
   ```
   # ensure to delete old stale versions
   docker image rm ghcr.io/icedevml/kms-csr-tool:master
   # run the tool
   docker run -it ghcr.io/icedevml/kms-csr-tool:master
   ```

2. The GCP authentication link will be generated, copy that link to your browser and perform authentication.
   After authentication is done, copy the authorization code from the browser and paste it into the shell.

3. Provide your GCP project ID, keyring location, keyring name and key name.

4. Complete the CSR generation form (provide your Organization Name etc).

5. The tool should display the generated CSR.
