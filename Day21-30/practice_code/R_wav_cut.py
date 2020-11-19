
import speech_recognition as sr
import os
import wave
import numpy as np


def CutFile(path, FileName, target_path):

    print("CutFile File Name is ", FileName)
    f = wave.open(path+"\\" + FileName, "rb")
    params = f.getparams()
    print(params)
    nchannels, sampwidth, framerate, nframes = params[:4]
    CutFrameNum = framerate * CutTimeDef
    # 讀取格式資訊
    # 一次性返回所有的WAV檔案的格式資訊，它返回的是一個組元(tuple)：聲道數, 量化位數（byte    單位）, 採
    # 樣頻率, 取樣點數, 壓縮型別, 壓縮型別的描述。wave模組只支援非壓縮的資料，因此可以忽略最後兩個資訊

    print("CutFrameNum=%d" % (CutFrameNum))
    print("nchannels=%d" % (nchannels))
    print("sampwidth=%d" % (sampwidth))
    print("framerate=%d" % (framerate))
    print("nframes=%d" % (nframes))
    str_data = f.readframes(nframes)
    f.close()  # 將波形資料轉換成陣列
    # Cutnum =nframes/framerate/CutTimeDef
    # 需要根據聲道數和量化單位，將讀取的二進位制資料轉換為一個可以計算的陣列
    wave_data = np.fromstring(str_data, dtype=np.short)
    wave_data.shape = -1, 2
    wave_data = wave_data.T
    temp_data = wave_data.T
    # StepNum = int(nframes/200)
    StepNum = CutFrameNum
    StepTotalNum = 0
    haha = 0
    while StepTotalNum < nframes:
        # for j in range(int(Cutnum)):
        print("Stemp=%d" % (haha))
        SaveFile = "%s-%03d.wav" % (FileName[:-4], (haha+1))
        print(FileName)
        temp_dataTemp = temp_data[StepNum * (haha):StepNum * (haha + 1)]
        haha = haha + 1
        StepTotalNum = haha * StepNum
        temp_dataTemp.shape = 1, -1
        temp_dataTemp = temp_dataTemp.astype(np.short)  # 開啟WAV文件
        f = wave.open(target_path + SaveFile, "wb")
        # 配置聲道數、量化位數和取樣頻率
        f.setnchannels(nchannels)
        f.setsampwidth(sampwidth)
        f.setframerate(framerate)
        # 將wav_data轉換為二進位制資料寫入檔案
        f.writeframes(temp_dataTemp.tostring())
        f.close()


def VoiceToText(path, files, target_path):
    for file in files:
        with open("%s\\%s.txt" % (target_path, file[:-4]), "w", encoding="utf-8") as f:
            f.write("%s:\n" % file)
            r = sr.Recognizer()  # 預設辨識英文
            with sr.WavFile(path+"\\"+file) as source:  # 讀取wav檔
                audio = r.record(source)
            try:
                text = r.recognize_google(audio, language="zh-TW")
                print(file)
                if len(text) == 0:
                    print("===無資料==")
                    continue

                print(text)
                f.write("%s \n\n" % text)
                if file == files[-1]:
                    print("結束翻譯")
            except sr.RequestError as e:
                print("無法翻譯{0}".format(e))
                # 兩個 except 是當語音辨識不出來的時候 防呆用的
                # 使用Google的服務
            except LookupError:
                print("Could not understand audio")
            except sr.UnknownValueError:
                print("Error: 無法識別 Audio")


def texts_to_one(path, target_file):
    files = os.listdir(path)
    with open(target_file, "w", encoding="utf-8") as f:
        for file in files:
            with open(os.path.join(path, file), "r", encoding='utf-8') as f2:
                f.write(f2.read())
    print("完成合併, 檔案位於 %s " % target_file)


if __name__ == "__main__":
    # # Cut Wave Setting
    CutTimeDef = 30  # 以1s截斷檔案
    # # CutFrameNum =0
    # FileName = "20201118.wav"
    # path = "g:\\"
    # target_path = "g:\\wav2\\"
    # CutFile(path, FileName, target_path)

    # path = "g:\\wav3\\"
    # target_path = "g:\\txt3\\"
    # files = os.listdir(path)
    # textfiles = os.listdir(target_path)
    # start_pos = 0
    # if len(textfiles) != 0:
    #     if files[-1][:-4] == textfiles[-1][:-4]:
    #         print("所有檔案，都已轉成語音")
    #     else:
    #         if len(textfiles) > 0:
    #             start_pos = files.index(textfiles[-1][:-4]+".wav")+1
    # files = files[start_pos:]
    # VoiceToText(path, files, target_path)
    path = "g:\\txt3\\"
    target_file = "g:\\text3.txt"
    texts_to_one(path, target_file)
