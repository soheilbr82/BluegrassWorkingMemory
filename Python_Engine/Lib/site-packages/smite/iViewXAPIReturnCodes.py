# -----------------------------------------------------------------------
#
# (c) Copyright 1997-2016, SensoMotoric Instruments GmbH
# 
# Permission  is  hereby granted,  free  of  charge,  to any  person  or
# organization  obtaining  a  copy  of  the  software  and  accompanying
# documentation  covered  by  this  license  (the  "Software")  to  use,
# reproduce,  display, distribute, execute,  and transmit  the Software,
# and  to  prepare derivative  works  of  the  Software, and  to  permit
# third-parties to whom the Software  is furnished to do so, all subject
# to the following:
# 
# The  copyright notices  in  the Software  and  this entire  statement,
# including the above license  grant, this restriction and the following
# disclaimer, must be  included in all copies of  the Software, in whole
# or  in part, and  all derivative  works of  the Software,  unless such
# copies   or   derivative   works   are   solely   in   the   form   of
# machine-executable  object   code  generated  by   a  source  language
# processor.
# 
# THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
# EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
# MERCHANTABILITY,   FITNESS  FOR  A   PARTICULAR  PURPOSE,   TITLE  AND
# NON-INFRINGEMENT. IN  NO EVENT SHALL  THE COPYRIGHT HOLDERS  OR ANYONE
# DISTRIBUTING  THE  SOFTWARE  BE   LIABLE  FOR  ANY  DAMAGES  OR  OTHER
# LIABILITY, WHETHER  IN CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT
# OF OR IN CONNECTION WITH THE  SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# -----------------------------------------------------------------------

def HandleError(ret):
    if ret == 1:
        return
    elif ret == 2:
        pass
        #msg = "no new data available"
    elif ret == 3:
        msg = "calibration or validation was aborted during progress"
    elif ret == 4:
        msg = "server is running"
    elif ret == 5:
        msg = "calibration is not in progress"
    elif ret == 11:
        msg = "window is open"        
    elif ret == 12:
        msg = "window is closed"        
    elif ret == 100:
        msg = "failed to establish connection"        
    elif ret == 101:
        msg = "no connection established"
    elif ret == 102:
        msg = "system is not calibrated"
    elif ret == 103:
        msg = "system is not validated"
    elif ret == 104:
        msg = "no eye tracking application running"
    elif ret == 105:
        msg = "failed to establish connection"
    elif ret == 111:
        msg = "no connection established"        
    elif ret == 112:
        msg = "parameter out of range"
    elif ret == 113:
        msg = "eye tracking device required for this calibration method is not connected"
    elif ret == 114:
        msg = "calibration timeout occurred"
    elif ret == 115:
        msg = "eye tracking is not stable"
    elif ret == 116:
        msg = "insufficient buffer size"
    elif ret == 121:
        msg = "cannot create socket"
    elif ret == 122:
        msg = "cannot connect with socket"        
    elif ret == 123:
        msg = "the defined port is blocked"
    elif ret == 124:
        msg = "failed to delete sockets"
    elif ret == 131:
        msg = "iView X (eyetracking-server) application was not able to response to current request"
    elif ret == 132:
        msg = "invalid version of iView X (eyetracking-server)"
    elif ret == 133:
        msg = "wrong version of iView X (eyetracking-server) application"
    elif ret == 171:
        msg = "failed to access log file"
    elif ret == 181:
        msg = "socket connection failed"
    elif ret == 201:
        msg = "Could not establish connection. Check if Eye Tracker is installed and running."
    elif ret == 191:
        msg = "recording buffer is empty"
    elif ret == 192:
        msg = "recording is activated"
    elif ret == 193:
        msg = "data buffer is full"
    elif ret == 194:
        msg = "iView X (eyetracking-server) application is not ready to record buffer"
    elif ret == 195:
        msg = "paused data buffer"
    elif ret == 201:
        msg = "iView X (eyetracking-server) application was not found"
    elif ret == 202:
        msg = "path for file does not exist"
    elif ret == 203:
        msg = "access denied"
    elif ret == 204:
        msg = "access incomplete"
    elif ret == 205:
        msg = "out of memory"
    elif ret == 211:
        msg = "failed to access eye tracking device"
    elif ret == 212:
        msg = "failed to access eye tracking device"
    elif ret == 213:
        msg = "failed to access port connected to eye tracking device"
    elif ret == 220:
        msg = "failed to open port"
    elif ret == 221:
        msg = "failed to close port"
    elif ret == 222:
        msg = "failed to access AOI data"
    elif ret == 223:
        msg = "AOI not defined"
    elif ret == 250:
        msg = "failed to access requested feature"
    elif ret == 300:
        msg = "function is deprecated"
    elif ret == 400:
        msg = "function or dll not initialized"
    else:
        msg = "Unknown return Code " + str(ret)
        
    if ret != 2:
        print(msg)
    