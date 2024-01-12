# Google Cloud KMS - CSR generation tool

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
   docker run -it icedevml/kms-csr-tool:build202401130057
   ```

2. The GCP authentication link will be generated, copy that link to your browser and perform authentication.
   After authentication is done, copy the authorization code from the browser and paste it into the shell.

3. Provide your GCP project ID, keyring location, keyring name and key name.

4. Complete the CSR generation form (provide your Organization Name etc).

5. The tool should display the generated CSR.
